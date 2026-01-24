"""
Shadow Sync Engine

Core sync engine that fetches Coda doc/page metadata and generates local shadow files.
"""

import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import re

from coda.clients.docs import CodaDocsClient
from coda.clients.pages import CodaPagesClient
from coda.shadow.shadow_config import ShadowConfig

logger = logging.getLogger(__name__)


def sanitize_filename(name: str) -> str:
    """
    Sanitize a string for use as a filename.
    
    Args:
        name: Original name
        
    Returns:
        Safe filename string
    """
    # Replace problematic characters with underscores
    safe = re.sub(r'[<>:"/\\|?*]', '_', name)
    # Collapse multiple underscores
    safe = re.sub(r'_+', '_', safe)
    # Trim and limit length
    safe = safe.strip('_')[:50]
    return safe or "unnamed"


class ShadowSync:
    """
    Engine for syncing Coda documents to local shadow files.
    
    Creates Markdown files with YAML frontmatter for each page,
    enabling fast local discovery via grep.
    
    Usage:
        config = ShadowConfig(
            shadow_dir=Path("/path/to/shadows"),
            doc_ids=["NDxZHneeIw"]
        )
        sync = ShadowSync(config)
        sync.run()
    """
    
    def __init__(self, config: ShadowConfig):
        """
        Initialize the sync engine.
        
        Args:
            config: ShadowConfig instance
        """
        self.config = config
        self.docs_client = CodaDocsClient()
        self.pages_client = CodaPagesClient()
        self._sync_stats: Dict[str, int] = {}
    
    def run(self) -> Dict[str, Any]:
        """
        Run a full sync of all configured docs.
        
        Returns:
            Dict with sync statistics
        """
        logger.info(f"Starting shadow sync for {len(self.config.doc_ids)} docs")
        start_time = time.time()
        
        # Ensure shadow directory exists
        self.config.shadow_dir.mkdir(parents=True, exist_ok=True)
        
        self._sync_stats = {
            "docs_synced": 0,
            "pages_synced": 0,
            "errors": 0,
        }
        
        all_docs: List[Dict[str, Any]] = []
        
        for doc_id in self.config.doc_ids:
            try:
                doc_info = self._sync_doc(doc_id)
                if doc_info:
                    all_docs.append(doc_info)
                    self._sync_stats["docs_synced"] += 1
            except Exception as e:
                logger.error(f"Failed to sync doc {doc_id}: {e}")
                self._sync_stats["errors"] += 1
        
        # Generate dashboard
        self._generate_dashboard(all_docs)
        
        elapsed = time.time() - start_time
        self._sync_stats["elapsed_seconds"] = round(elapsed, 2)
        
        logger.info(f"Shadow sync complete: {self._sync_stats}")
        return self._sync_stats
    
    def _sync_doc(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """
        Sync a single document and its pages.
        
        Args:
            doc_id: Coda document ID
            
        Returns:
            Doc info dict or None on failure
        """
        logger.info(f"Syncing doc {doc_id}")
        
        # Get doc metadata
        doc = self.docs_client.get_doc(doc_id)
        doc_name = doc.get("name", "Untitled")
        
        # Create doc-specific shadow directory
        safe_doc_name = sanitize_filename(doc_name)
        doc_dir = self.config.shadow_dir / f"{safe_doc_name}_{doc_id[:8]}"
        doc_dir.mkdir(parents=True, exist_ok=True)
        
        # Get pages
        pages = self.pages_client.list_pages(
            doc_id,
            limit=self.config.max_pages_per_doc
        )
        
        page_infos: List[Dict[str, Any]] = []
        
        for page in pages:
            try:
                page_info = self._sync_page(doc_id, doc_name, page, doc_dir)
                if page_info:
                    page_infos.append(page_info)
                    self._sync_stats["pages_synced"] += 1
            except Exception as e:
                logger.warning(f"Failed to sync page {page.get('id')}: {e}")
                self._sync_stats["errors"] += 1
        
        # Create doc index file
        self._generate_doc_index(doc, page_infos, doc_dir)
        
        return {
            "doc_id": doc_id,
            "doc_name": doc_name,
            "doc_dir": doc_dir,
            "page_count": len(page_infos),
            "pages": page_infos,
        }
    
    def _sync_page(
        self,
        doc_id: str,
        doc_name: str,
        page: Dict[str, Any],
        doc_dir: Path
    ) -> Optional[Dict[str, Any]]:
        """
        Sync a single page to a shadow file.
        
        Args:
            doc_id: Document ID
            doc_name: Document name
            page: Page metadata from API
            doc_dir: Directory for this doc's shadows
            
        Returns:
            Page info dict or None
        """
        page_id = page.get("id", "")
        page_name = page.get("name", "Untitled")
        
        # Get detailed page info
        page_detail = self.pages_client.get_page(doc_id, page_id)
        
        # Build YAML frontmatter
        now_iso = datetime.now(timezone.utc).isoformat()
        
        frontmatter = f"""---
coda_doc_id: "{doc_id}"
coda_page_id: "{page_id}"
doc_name: "{doc_name}"
page_name: "{page_name}"
last_synced: "{now_iso}"
content_type: "{page_detail.get('contentType', 'unknown')}"
subtitle: "{page_detail.get('subtitle', '')}"
icon: "{page_detail.get('icon', {}).get('name', '')}"
browser_link: "{page_detail.get('browserLink', '')}"
---
"""
        
        # Build content section
        content_lines = [
            f"# {page_name}",
            "",
        ]
        
        if page_detail.get("subtitle"):
            content_lines.append(f"*{page_detail['subtitle']}*")
            content_lines.append("")
        
        # Add navigation link
        browser_link = page_detail.get("browserLink", "")
        if browser_link:
            content_lines.append(f"[Open in Coda →]({browser_link})")
            content_lines.append("")
        
        # Optionally fetch page content
        if self.config.include_content:
            try:
                page_content = self.pages_client.list_page_content(
                    doc_id, page_id, limit=50
                )
                if page_content:
                    content_lines.append("## Content Preview")
                    content_lines.append("")
                    for item in page_content[:10]:  # First 10 elements
                        text = item.get("value", "")
                        if text:
                            content_lines.append(text)
                    if len(page_content) > 10:
                        content_lines.append(f"... and {len(page_content) - 10} more elements")
            except Exception as e:
                logger.debug(f"Could not fetch content for {page_id}: {e}")
        
        # Write shadow file
        safe_page_name = sanitize_filename(page_name)
        shadow_path = doc_dir / f"{safe_page_name}_{page_id[:8]}.md"
        
        with open(shadow_path, "w", encoding="utf-8") as f:
            f.write(frontmatter)
            f.write("\n".join(content_lines))
        
        logger.debug(f"Created shadow: {shadow_path}")
        
        return {
            "page_id": page_id,
            "page_name": page_name,
            "shadow_path": shadow_path,
            "browser_link": browser_link,
        }
    
    def _generate_doc_index(
        self,
        doc: Dict[str, Any],
        page_infos: List[Dict[str, Any]],
        doc_dir: Path
    ) -> Path:
        """
        Generate an index file for a document.
        
        Args:
            doc: Document metadata
            page_infos: List of synced page info dicts
            doc_dir: Document shadow directory
            
        Returns:
            Path to generated index file
        """
        doc_name = doc.get("name", "Untitled")
        doc_id = doc.get("id", "")
        
        lines = [
            f"# {doc_name}",
            "",
            f"**Doc ID**: `{doc_id}`",
            f"**Pages**: {len(page_infos)}",
            f"**Last Synced**: {datetime.now(timezone.utc).isoformat()}",
            "",
            "## Pages",
            "",
        ]
        
        for page in page_infos:
            page_name = page["page_name"]
            shadow_path = page["shadow_path"]
            relative_path = shadow_path.name
            lines.append(f"- [{page_name}]({relative_path})")
        
        index_path = doc_dir / "_index.md"
        with open(index_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        
        return index_path
    
    def _generate_dashboard(self, all_docs: List[Dict[str, Any]]) -> Path:
        """
        Generate the main dashboard index.
        
        Args:
            all_docs: List of all synced doc info dicts
            
        Returns:
            Path to dashboard file
        """
        lines = [
            "# Coda Shadow Dashboard",
            "",
            f"**Last Synced**: {datetime.now(timezone.utc).isoformat()}",
            f"**Documents**: {len(all_docs)}",
            f"**Total Pages**: {sum(d['page_count'] for d in all_docs)}",
            "",
            "## Documents",
            "",
        ]
        
        for doc in all_docs:
            doc_name = doc["doc_name"]
            doc_dir = doc["doc_dir"]
            page_count = doc["page_count"]
            relative_dir = doc_dir.name
            lines.append(f"### [{doc_name}]({relative_dir}/_index.md)")
            lines.append(f"*{page_count} pages*")
            lines.append("")
        
        lines.extend([
            "---",
            "",
            "*Generated by PAI Shadow Sync*",
        ])
        
        dashboard_path = self.config.shadow_dir / "dashboard.md"
        with open(dashboard_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        
        logger.info(f"Generated dashboard: {dashboard_path}")
        return dashboard_path
    
    def sync_doc(self, doc_id: str) -> Dict[str, Any]:
        """
        Sync a single document (incremental sync).
        
        Args:
            doc_id: Coda document ID
            
        Returns:
            Sync result for this doc
        """
        self._sync_stats = {"docs_synced": 0, "pages_synced": 0, "errors": 0}
        
        self.config.shadow_dir.mkdir(parents=True, exist_ok=True)
        
        result = self._sync_doc(doc_id)
        if result:
            self._sync_stats["docs_synced"] = 1
            return result
        
        return {"error": "Sync failed", "doc_id": doc_id}
