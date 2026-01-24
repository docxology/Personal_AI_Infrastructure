"""
Shadow Index

Local index management for shadow files.
Provides fast lookups by doc ID, page ID, or category.
"""

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional
import yaml

logger = logging.getLogger(__name__)


@dataclass
class ShadowEntry:
    """
    Represents a single shadow file entry.
    """
    shadow_path: Path
    coda_doc_id: str
    coda_page_id: str
    doc_name: str
    page_name: str
    last_synced: str
    content_type: str = ""
    subtitle: str = ""
    browser_link: str = ""
    synopsis: str = ""


@dataclass
class ShadowIndex:
    """
    In-memory index of shadow files for fast lookups.
    
    Usage:
        index = ShadowIndex.from_directory(Path("/path/to/shadows"))
        
        # Lookup by doc ID
        pages = index.get_pages_for_doc("NDxZHneeIw")
        
        # Lookup by page ID
        entry = index.get_by_page_id("canvas-abc123")
    """
    entries: List[ShadowEntry] = field(default_factory=list)
    _by_doc_id: Dict[str, List[ShadowEntry]] = field(default_factory=dict)
    _by_page_id: Dict[str, ShadowEntry] = field(default_factory=dict)
    
    def __post_init__(self):
        """Build lookup indices."""
        self._rebuild_indices()
    
    def _rebuild_indices(self) -> None:
        """Rebuild internal lookup indices."""
        self._by_doc_id.clear()
        self._by_page_id.clear()
        
        for entry in self.entries:
            # Index by doc
            if entry.coda_doc_id not in self._by_doc_id:
                self._by_doc_id[entry.coda_doc_id] = []
            self._by_doc_id[entry.coda_doc_id].append(entry)
            
            # Index by page
            self._by_page_id[entry.coda_page_id] = entry
    
    @classmethod
    def from_directory(cls, shadow_dir: Path) -> "ShadowIndex":
        """
        Build an index by scanning a shadow directory.
        
        Args:
            shadow_dir: Root shadow directory
            
        Returns:
            ShadowIndex instance
        """
        logger.info(f"Building shadow index from {shadow_dir}")
        entries: List[ShadowEntry] = []
        
        if not shadow_dir.exists():
            logger.warning(f"Shadow directory does not exist: {shadow_dir}")
            return cls(entries=[])
        
        # Find all .md files (excluding index files)
        for md_file in shadow_dir.rglob("*.md"):
            if md_file.name.startswith("_") or md_file.name == "dashboard.md":
                continue
            
            entry = cls._parse_shadow_file(md_file)
            if entry:
                entries.append(entry)
        
        logger.info(f"Indexed {len(entries)} shadow files")
        return cls(entries=entries)
    
    @classmethod
    def _parse_shadow_file(cls, path: Path) -> Optional[ShadowEntry]:
        """
        Parse a shadow file and extract frontmatter.
        
        Args:
            path: Path to shadow file
            
        Returns:
            ShadowEntry or None if parsing fails
        """
        try:
            content = path.read_text(encoding="utf-8")
            
            # Extract YAML frontmatter
            match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                return None
            
            frontmatter = yaml.safe_load(match.group(1))
            if not frontmatter:
                return None
            
            return ShadowEntry(
                shadow_path=path,
                coda_doc_id=frontmatter.get("coda_doc_id", ""),
                coda_page_id=frontmatter.get("coda_page_id", ""),
                doc_name=frontmatter.get("doc_name", ""),
                page_name=frontmatter.get("page_name", ""),
                last_synced=frontmatter.get("last_synced", ""),
                content_type=frontmatter.get("content_type", ""),
                subtitle=frontmatter.get("subtitle", ""),
                browser_link=frontmatter.get("browser_link", ""),
                synopsis=frontmatter.get("synopsis", ""),
            )
        except Exception as e:
            logger.debug(f"Failed to parse {path}: {e}")
            return None
    
    def get_pages_for_doc(self, doc_id: str) -> List[ShadowEntry]:
        """
        Get all shadow entries for a document.
        
        Args:
            doc_id: Coda document ID
            
        Returns:
            List of ShadowEntry for the doc
        """
        return self._by_doc_id.get(doc_id, [])
    
    def get_by_page_id(self, page_id: str) -> Optional[ShadowEntry]:
        """
        Get a shadow entry by page ID.
        
        Args:
            page_id: Coda page ID
            
        Returns:
            ShadowEntry or None
        """
        return self._by_page_id.get(page_id)
    
    def get_all_doc_ids(self) -> List[str]:
        """Get all unique document IDs in the index."""
        return list(self._by_doc_id.keys())
    
    def search_by_name(self, query: str) -> List[ShadowEntry]:
        """
        Search entries by page or doc name.
        
        Args:
            query: Search query (case-insensitive)
            
        Returns:
            List of matching entries
        """
        query_lower = query.lower()
        return [
            e for e in self.entries
            if query_lower in e.page_name.lower() or query_lower in e.doc_name.lower()
        ]
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Export index as a dictionary.
        
        Returns:
            Dict representation of the index
        """
        return {
            "total_entries": len(self.entries),
            "docs": {
                doc_id: [
                    {
                        "page_id": e.coda_page_id,
                        "page_name": e.page_name,
                        "shadow_path": str(e.shadow_path),
                    }
                    for e in entries
                ]
                for doc_id, entries in self._by_doc_id.items()
            }
        }
