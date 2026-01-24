"""
Shadow Search

Fast local search utilities for shadow files using grep-like operations.
"""

import logging
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

logger = logging.getLogger(__name__)


@dataclass
class ShadowSearchResult:
    """
    Represents a search result from shadow files.
    """
    shadow_path: Path
    line_number: int
    line_content: str
    doc_name: str = ""
    page_name: str = ""
    coda_doc_id: str = ""
    coda_page_id: str = ""
    browser_link: str = ""


def shadow_search(
    shadow_dir: Path,
    query: str,
    case_sensitive: bool = False,
    max_results: int = 50,
    file_pattern: str = "*.md"
) -> List[ShadowSearchResult]:
    """
    Search shadow files for a query string.
    
    Uses grep for fast searching when available, falls back to Python.
    
    Args:
        shadow_dir: Root shadow directory
        query: Search query
        case_sensitive: Whether to match case
        max_results: Maximum results to return
        file_pattern: Glob pattern for files to search
        
    Returns:
        List of ShadowSearchResult
    """
    if not shadow_dir.exists():
        logger.warning(f"Shadow directory does not exist: {shadow_dir}")
        return []
    
    # Try grep first (much faster)
    try:
        return _grep_search(shadow_dir, query, case_sensitive, max_results)
    except (subprocess.SubprocessError, FileNotFoundError):
        logger.debug("grep not available, falling back to Python search")
        return _python_search(shadow_dir, query, case_sensitive, max_results, file_pattern)


def _grep_search(
    shadow_dir: Path,
    query: str,
    case_sensitive: bool,
    max_results: int
) -> List[ShadowSearchResult]:
    """
    Search using grep command.
    
    Args:
        shadow_dir: Root shadow directory
        query: Search query
        case_sensitive: Whether to match case
        max_results: Maximum results to return
        
    Returns:
        List of ShadowSearchResult
    """
    cmd = ["grep", "-rn"]
    if not case_sensitive:
        cmd.append("-i")
    cmd.extend(["--include=*.md", query, str(shadow_dir)])
    
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=10
    )
    
    results: List[ShadowSearchResult] = []
    
    for line in result.stdout.splitlines()[:max_results]:
        # Parse grep output: filename:line_number:content
        match = re.match(r'^(.+?):(\d+):(.*)$', line)
        if match:
            path = Path(match.group(1))
            line_num = int(match.group(2))
            content = match.group(3)
            
            # Extract metadata from file
            metadata = _extract_metadata(path)
            
            results.append(ShadowSearchResult(
                shadow_path=path,
                line_number=line_num,
                line_content=content.strip(),
                **metadata
            ))
    
    logger.debug(f"grep found {len(results)} results for '{query}'")
    return results


def _python_search(
    shadow_dir: Path,
    query: str,
    case_sensitive: bool,
    max_results: int,
    file_pattern: str
) -> List[ShadowSearchResult]:
    """
    Search using pure Python (fallback).
    
    Args:
        shadow_dir: Root shadow directory
        query: Search query
        case_sensitive: Whether to match case
        max_results: Maximum results to return
        file_pattern: Glob pattern for files to search
        
    Returns:
        List of ShadowSearchResult
    """
    results: List[ShadowSearchResult] = []
    search_query = query if case_sensitive else query.lower()
    
    for md_file in shadow_dir.rglob(file_pattern):
        if len(results) >= max_results:
            break
        
        try:
            content = md_file.read_text(encoding="utf-8")
            lines = content.splitlines()
            
            for i, line in enumerate(lines, 1):
                compare_line = line if case_sensitive else line.lower()
                
                if search_query in compare_line:
                    metadata = _extract_metadata(md_file)
                    results.append(ShadowSearchResult(
                        shadow_path=md_file,
                        line_number=i,
                        line_content=line.strip(),
                        **metadata
                    ))
                    
                    if len(results) >= max_results:
                        break
        except Exception as e:
            logger.debug(f"Error reading {md_file}: {e}")
    
    logger.debug(f"Python search found {len(results)} results for '{query}'")
    return results


def _extract_metadata(path: Path) -> dict:
    """
    Extract frontmatter metadata from a shadow file.
    
    Args:
        path: Path to shadow file
        
    Returns:
        Dict with doc_name, page_name, coda_doc_id, coda_page_id, browser_link
    """
    metadata = {
        "doc_name": "",
        "page_name": "",
        "coda_doc_id": "",
        "coda_page_id": "",
        "browser_link": "",
    }
    
    try:
        content = path.read_text(encoding="utf-8")
        
        # Quick regex extraction from frontmatter
        for key in ["doc_name", "page_name", "coda_doc_id", "coda_page_id", "browser_link"]:
            match = re.search(rf'^{key}:\s*"(.+?)"', content, re.MULTILINE)
            if match:
                metadata[key] = match.group(1)
    except Exception:
        pass
    
    return metadata


def search_by_doc(
    shadow_dir: Path,
    doc_id: str,
    query: Optional[str] = None
) -> List[ShadowSearchResult]:
    """
    Search within a specific document's shadows.
    
    Args:
        shadow_dir: Root shadow directory
        doc_id: Coda document ID to search within
        query: Optional search query (if None, returns all pages)
        
    Returns:
        List of ShadowSearchResult
    """
    # Find doc directory
    doc_dirs = list(shadow_dir.glob(f"*_{doc_id[:8]}"))
    if not doc_dirs:
        logger.warning(f"No shadow directory found for doc {doc_id}")
        return []
    
    doc_dir = doc_dirs[0]
    
    if query:
        return shadow_search(doc_dir, query)
    else:
        # Return all pages in this doc
        results: List[ShadowSearchResult] = []
        for md_file in doc_dir.glob("*.md"):
            if md_file.name.startswith("_"):
                continue
            metadata = _extract_metadata(md_file)
            results.append(ShadowSearchResult(
                shadow_path=md_file,
                line_number=0,
                line_content="",
                **metadata
            ))
        return results
