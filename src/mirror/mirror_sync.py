"""
Mirror Sync Orchestrator

Unified orchestrator for triple-mirroring knowledge bases.
"""

import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

from mirror.mirror_config import MirrorConfig
from mirror.mirror_coda import CodaMirror
from mirror.mirror_github import GitHubMirror
from mirror.mirror_drive import DriveMirror

logger = logging.getLogger(__name__)


@dataclass
class SyncResult:
    """Result from a sync operation."""
    target: str
    success: bool
    stats: Dict[str, Any]
    error: Optional[str] = None
    elapsed_seconds: float = 0.0


class MirrorSync:
    """
    Unified orchestrator for triple-mirroring.
    
    Syncs knowledge base to:
    - Coda (document pages)
    - GitHub (version-controlled repo)
    - Google Drive (cloud files)
    
    Usage:
        config = MirrorConfig(source_dir=Path("~/.pai/knowledge"))
        sync = MirrorSync(config)
        results = sync.sync_all()
    """
    
    def __init__(self, config: MirrorConfig):
        """
        Initialize the orchestrator.
        
        Args:
            config: MirrorConfig with all settings
        """
        self.config = config
        
        # Initialize mirrors (lazy)
        self._coda: Optional[CodaMirror] = None
        self._github: Optional[GitHubMirror] = None
        self._drive: Optional[DriveMirror] = None
    
    @property
    def coda(self) -> CodaMirror:
        if self._coda is None:
            self._coda = CodaMirror(doc_id=self.config.coda_doc_id)
        return self._coda
    
    @property
    def github(self) -> GitHubMirror:
        if self._github is None:
            self._github = GitHubMirror(
                repo=self.config.github_repo,
                branch=self.config.github_branch
            )
        return self._github
    
    @property
    def drive(self) -> DriveMirror:
        if self._drive is None:
            self._drive = DriveMirror(folder_id=self.config.drive_folder_id)
        return self._drive
    
    def sync_all(self) -> Dict[str, SyncResult]:
        """
        Sync to all enabled targets.
        
        Returns:
            Dict mapping target name to SyncResult
        """
        logger.info("Starting triple mirror sync")
        results = {}
        
        if self.config.enable_coda:
            results["coda"] = self.sync_coda()
        
        if self.config.enable_github:
            results["github"] = self.sync_github()
        
        if self.config.enable_drive:
            results["drive"] = self.sync_drive()
        
        # Log summary
        success_count = sum(1 for r in results.values() if r.success)
        logger.info(f"Triple mirror complete: {success_count}/{len(results)} targets succeeded")
        
        return results
    
    def sync_coda(self) -> SyncResult:
        """
        Sync to Coda.
        
        Returns:
            SyncResult for Coda
        """
        import time
        start = time.time()
        
        try:
            logger.info(f"Syncing to Coda doc {self.config.coda_doc_id}")
            stats = self.coda.sync(self.config.source_dir)
            return SyncResult(
                target="coda",
                success=stats.get("success", True),
                stats=stats,
                elapsed_seconds=round(time.time() - start, 2)
            )
        except Exception as e:
            logger.error(f"Coda sync failed: {e}")
            return SyncResult(
                target="coda",
                success=False,
                stats={},
                error=str(e),
                elapsed_seconds=round(time.time() - start, 2)
            )
    
    def sync_github(self) -> SyncResult:
        """
        Sync to GitHub.
        
        Returns:
            SyncResult for GitHub
        """
        import time
        start = time.time()
        
        try:
            logger.info(f"Syncing to GitHub {self.config.github_repo}")
            stats = self.github.sync(
                self.config.source_dir,
                commit_message=self.config.auto_commit_message
            )
            return SyncResult(
                target="github",
                success=stats.get("success", True),
                stats=stats,
                elapsed_seconds=round(time.time() - start, 2)
            )
        except Exception as e:
            logger.error(f"GitHub sync failed: {e}")
            return SyncResult(
                target="github",
                success=False,
                stats={},
                error=str(e),
                elapsed_seconds=round(time.time() - start, 2)
            )
    
    def sync_drive(self) -> SyncResult:
        """
        Sync to Google Drive.
        
        Returns:
            SyncResult for Drive
        """
        import time
        start = time.time()
        
        try:
            logger.info("Syncing to Google Drive")
            stats = self.drive.sync(self.config.source_dir)
            return SyncResult(
                target="drive",
                success=stats.get("success", True),
                stats=stats,
                elapsed_seconds=round(time.time() - start, 2)
            )
        except Exception as e:
            logger.error(f"Drive sync failed: {e}")
            return SyncResult(
                target="drive",
                success=False,
                stats={},
                error=str(e),
                elapsed_seconds=round(time.time() - start, 2)
            )
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get current status of all mirrors.
        
        Returns:
            Status dict with target states
        """
        return {
            "source_dir": str(self.config.source_dir),
            "source_exists": self.config.source_dir.exists(),
            "targets": {
                "coda": {
                    "enabled": self.config.enable_coda,
                    "doc_id": self.config.coda_doc_id,
                },
                "github": {
                    "enabled": self.config.enable_github,
                    "repo": self.config.github_repo,
                    "branch": self.config.github_branch,
                },
                "drive": {
                    "enabled": self.config.enable_drive,
                    "folder_id": self.config.drive_folder_id,
                },
            }
        }


def quick_sync(source_dir: Optional[Path] = None) -> Dict[str, SyncResult]:
    """
    Quick triple sync with defaults.
    
    Args:
        source_dir: Source directory (default: ~/.pai/knowledge)
        
    Returns:
        Dict of sync results
    """
    from mirror.mirror_config import get_default_config
    
    config = get_default_config()
    if source_dir:
        config.source_dir = source_dir
    
    sync = MirrorSync(config)
    return sync.sync_all()
