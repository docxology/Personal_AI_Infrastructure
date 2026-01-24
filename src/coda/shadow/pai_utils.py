"""
PAI Utilities for Coda Shadow Sync

Integrated workflows for shadow sync with PAI capabilities:
- Summary generation for daily/weekly reports
- Email integration for status updates
- Scheduled sync utilities
"""

import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from coda.shadow.shadow_config import ShadowConfig, DEFAULT_SHADOW_DIR
from coda.shadow.shadow_sync import ShadowSync
from coda.shadow.shadow_index import ShadowIndex, ShadowEntry
from coda.shadow.shadow_search import shadow_search, ShadowSearchResult

logger = logging.getLogger(__name__)

# PAI Document Controller ID
PAI_DOC_ID = "NDxZHneeIw"


def get_default_config() -> ShadowConfig:
    """
    Get the default PAI shadow configuration.
    
    Returns:
        ShadowConfig with PAI defaults
    """
    return ShadowConfig(
        shadow_dir=DEFAULT_SHADOW_DIR,
        doc_ids=[PAI_DOC_ID],
        sync_interval_hours=24,
        include_content=True,
    )


def sync_pai_shadows(
    config: Optional[ShadowConfig] = None,
    max_pages: int = 50
) -> Dict[str, Any]:
    """
    Sync PAI Document Controller to local shadows.
    
    This is the primary entry point for PAI shadow sync.
    
    Args:
        config: Optional custom config (uses PAI defaults if not provided)
        max_pages: Maximum pages per document
        
    Returns:
        Sync statistics dict
    """
    if config is None:
        config = get_default_config()
    
    config.max_pages_per_doc = max_pages
    
    logger.info("Starting PAI shadow sync...")
    sync = ShadowSync(config)
    stats = sync.run()
    logger.info(f"PAI shadow sync complete: {stats}")
    
    return stats


def generate_shadow_summary(
    shadow_dir: Optional[Path] = None,
    include_content: bool = True
) -> str:
    """
    Generate a Markdown summary of the shadow index.
    
    Useful for daily/weekly status emails.
    
    Args:
        shadow_dir: Shadow directory path (uses default if not provided)
        include_content: Include page content preview
        
    Returns:
        Markdown-formatted summary
    """
    if shadow_dir is None:
        shadow_dir = DEFAULT_SHADOW_DIR
    
    index = ShadowIndex.from_directory(shadow_dir)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    lines = [
        "# Coda Shadow Index Summary",
        "",
        f"**Generated**: {now}",
        f"**Shadow Directory**: `{shadow_dir}`",
        f"**Total Pages**: {len(index.entries)}",
        f"**Documents**: {len(index.get_all_doc_ids())}",
        "",
    ]
    
    # Group by document
    for doc_id in index.get_all_doc_ids():
        pages = index.get_pages_for_doc(doc_id)
        if not pages:
            continue
        
        doc_name = pages[0].doc_name if pages else doc_id
        lines.append(f"## {doc_name}")
        lines.append(f"*Doc ID: `{doc_id}` | {len(pages)} pages*")
        lines.append("")
        
        for page in pages[:10]:  # Limit to 10 pages per doc
            lines.append(f"- **{page.page_name}**")
            if page.subtitle:
                lines.append(f"  - {page.subtitle}")
            if page.browser_link:
                lines.append(f"  - [Open in Coda]({page.browser_link})")
        
        if len(pages) > 10:
            lines.append(f"- *... and {len(pages) - 10} more pages*")
        lines.append("")
    
    return "\n".join(lines)


def generate_daily_digest_content(
    shadow_dir: Optional[Path] = None,
    recent_query: Optional[str] = None
) -> str:
    """
    Generate content for a daily digest email.
    
    Args:
        shadow_dir: Shadow directory path
        recent_query: Optional query to highlight recent items
        
    Returns:
        HTML-formatted email content
    """
    if shadow_dir is None:
        shadow_dir = DEFAULT_SHADOW_DIR
    
    index = ShadowIndex.from_directory(shadow_dir)
    now = datetime.now(timezone.utc)
    
    # Build HTML content
    html_parts = [
        "<h2>📊 Daily Coda Shadow Digest</h2>",
        f"<p><em>Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}</em></p>",
        "<hr>",
    ]
    
    # Summary stats
    html_parts.append("<h3>Shadow Index Stats</h3>")
    html_parts.append("<ul>")
    html_parts.append(f"<li><strong>Total Pages</strong>: {len(index.entries)}</li>")
    html_parts.append(f"<li><strong>Documents</strong>: {len(index.get_all_doc_ids())}</li>")
    html_parts.append("</ul>")
    
    # Recent search results if query provided
    if recent_query:
        results = shadow_search(shadow_dir, recent_query, max_results=5)
        if results:
            html_parts.append(f"<h3>🔍 Search: \"{recent_query}\"</h3>")
            html_parts.append("<ul>")
            for r in results:
                link = r.browser_link if r.browser_link else "#"
                html_parts.append(
                    f"<li><a href='{link}'>{r.page_name}</a>: {r.line_content[:100]}...</li>"
                )
            html_parts.append("</ul>")
    
    # Document list
    html_parts.append("<h3>📁 Indexed Documents</h3>")
    html_parts.append("<ul>")
    for doc_id in index.get_all_doc_ids():
        pages = index.get_pages_for_doc(doc_id)
        if pages:
            doc_name = pages[0].doc_name
            html_parts.append(f"<li><strong>{doc_name}</strong> ({len(pages)} pages)</li>")
    html_parts.append("</ul>")
    
    html_parts.append("<hr>")
    html_parts.append("<p><em>Generated by PAI Shadow Sync</em></p>")
    
    return "\n".join(html_parts)


def generate_weekly_report_content(
    shadow_dir: Optional[Path] = None
) -> str:
    """
    Generate content for a weekly report email.
    
    Args:
        shadow_dir: Shadow directory path
        
    Returns:
        HTML-formatted email content
    """
    if shadow_dir is None:
        shadow_dir = DEFAULT_SHADOW_DIR
    
    index = ShadowIndex.from_directory(shadow_dir)
    now = datetime.now(timezone.utc)
    
    html_parts = [
        "<h2>📅 Weekly Coda Knowledge Report</h2>",
        f"<p><em>Week of {now.strftime('%Y-%m-%d')}</em></p>",
        "<hr>",
    ]
    
    # Full summary
    html_parts.append("<h3>📊 Knowledge Base Overview</h3>")
    html_parts.append("<table border='1' cellpadding='8'>")
    html_parts.append("<tr><th>Metric</th><th>Value</th></tr>")
    html_parts.append(f"<tr><td>Total Indexed Pages</td><td>{len(index.entries)}</td></tr>")
    html_parts.append(f"<tr><td>Documents Tracked</td><td>{len(index.get_all_doc_ids())}</td></tr>")
    html_parts.append(f"<tr><td>Shadow Directory</td><td><code>{shadow_dir}</code></td></tr>")
    html_parts.append("</table>")
    
    # Detailed document breakdown
    html_parts.append("<h3>📁 Document Details</h3>")
    
    for doc_id in index.get_all_doc_ids():
        pages = index.get_pages_for_doc(doc_id)
        if not pages:
            continue
        
        doc_name = pages[0].doc_name
        html_parts.append(f"<h4>{doc_name}</h4>")
        html_parts.append(f"<p><em>Doc ID: {doc_id} | {len(pages)} pages</em></p>")
        html_parts.append("<ul>")
        
        for page in pages:
            link = page.browser_link if page.browser_link else "#"
            html_parts.append(f"<li><a href='{link}'>{page.page_name}</a></li>")
        
        html_parts.append("</ul>")
    
    html_parts.append("<hr>")
    html_parts.append("<p><em>Part of PAI - Personal AI Infrastructure</em></p>")
    
    return "\n".join(html_parts)


def send_shadow_digest_email(
    to: str,
    subject_prefix: str = "[PAI Shadow]",
    digest_type: str = "daily",
    query: Optional[str] = None
) -> Dict[str, Any]:
    """
    Send a shadow digest email via Gmail.
    
    Args:
        to: Recipient email address
        subject_prefix: Email subject prefix
        digest_type: "daily" or "weekly"
        query: Optional search query to include
        
    Returns:
        Gmail send result
        
    Raises:
        ImportError: If Gmail client not available
    """
    try:
        from google.gmail.client import GoogleGmailClient
    except ImportError:
        raise ImportError("Gmail client not available. Install google module dependencies.")
    
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    if digest_type == "weekly":
        subject = f"{subject_prefix} Weekly Knowledge Report - {now}"
        body = generate_weekly_report_content()
    else:
        subject = f"{subject_prefix} Daily Digest - {now}"
        body = generate_daily_digest_content(recent_query=query)
    
    gmail = GoogleGmailClient()
    result = gmail.send_email(
        to=to,
        subject=subject,
        body=body,
        is_html=True
    )
    
    logger.info(f"Sent {digest_type} shadow digest to {to}")
    return result


def quick_search(query: str, max_results: int = 10) -> List[ShadowSearchResult]:
    """
    Quick local search across PAI shadows.
    
    Args:
        query: Search query
        max_results: Maximum results to return
        
    Returns:
        List of search results
    """
    return shadow_search(DEFAULT_SHADOW_DIR, query, max_results=max_results)


def get_shadow_stats() -> Dict[str, Any]:
    """
    Get current shadow index statistics.
    
    Returns:
        Dict with stats including page counts and doc IDs
    """
    index = ShadowIndex.from_directory(DEFAULT_SHADOW_DIR)
    
    return {
        "shadow_dir": str(DEFAULT_SHADOW_DIR),
        "total_pages": len(index.entries),
        "total_docs": len(index.get_all_doc_ids()),
        "doc_ids": index.get_all_doc_ids(),
        "docs": {
            doc_id: len(index.get_pages_for_doc(doc_id))
            for doc_id in index.get_all_doc_ids()
        }
    }
