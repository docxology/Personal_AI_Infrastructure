"""
GitHub Mirror

Mirror knowledge base to a GitHub repository.
"""

import logging
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from git.core import GitClient, get_repo_root
from git.github import GitHubClient

logger = logging.getLogger(__name__)


class GitHubMirror:
    """
    Mirror knowledge files to a GitHub repository.
    
    Supports:
    - Cloning/updating target repo
    - Copying knowledge files
    - Committing and pushing changes
    - Auto-creating repo if needed
    
    Usage:
        mirror = GitHubMirror("GithubBlanket/pai-knowledge")
        result = mirror.sync(source_dir=Path("~/.pai/knowledge"))
    """
    
    def __init__(
        self,
        repo: str,
        branch: str = "main",
        clone_dir: Optional[Path] = None
    ):
        """
        Initialize GitHub mirror.
        
        Args:
            repo: Repository in owner/name format
            branch: Target branch
            clone_dir: Local clone directory (default: temp)
        """
        self.repo = repo
        self.branch = branch
        self.owner, self.repo_name = repo.split("/")
        self.clone_dir = clone_dir or Path(tempfile.gettempdir()) / f"mirror_{self.repo_name}"
        
        self.github = GitHubClient()
        self._git: Optional[GitClient] = None
    
    def _ensure_repo_exists(self) -> bool:
        """
        Ensure GitHub repository exists, create if not.
        
        Returns:
            True if repo exists or was created
        """
        try:
            self.github.get_repo(self.owner, self.repo_name)
            logger.debug(f"Repo {self.repo} exists")
            return True
        except Exception:
            logger.info(f"Creating repo {self.repo_name}")
            self.github.create_repo(
                name=self.repo_name,
                description="PAI Knowledge Base Mirror",
                private=True,
                auto_init=True
            )
            return True
    
    def _clone_or_pull(self) -> GitClient:
        """
        Clone repo if needed, otherwise pull latest.
        
        Returns:
            GitClient for the repo
        """
        if self.clone_dir.exists() and (self.clone_dir / ".git").exists():
            # Pull latest
            logger.debug(f"Pulling latest in {self.clone_dir}")
            git = GitClient(str(self.clone_dir))
            try:
                git.pull("origin", self.branch)
            except Exception as e:
                logger.warning(f"Pull failed (may be new repo): {e}")
            return git
        else:
            # Clone
            self.clone_dir.mkdir(parents=True, exist_ok=True)
            clone_url = f"https://github.com/{self.repo}.git"
            logger.info(f"Cloning {clone_url} to {self.clone_dir}")
            
            import subprocess
            subprocess.run(
                ["git", "clone", "-b", self.branch, clone_url, str(self.clone_dir)],
                check=True,
                capture_output=True
            )
            return GitClient(str(self.clone_dir))
    
    def sync(
        self,
        source_dir: Path,
        commit_message: Optional[str] = None,
        push: bool = True
    ) -> Dict[str, Any]:
        """
        Sync knowledge files to GitHub.
        
        Args:
            source_dir: Source directory to mirror
            commit_message: Custom commit message
            push: Push after commit
            
        Returns:
            Sync result with stats
        """
        logger.info(f"Syncing {source_dir} to {self.repo}")
        
        if not source_dir.exists():
            return {"success": False, "error": f"Source not found: {source_dir}"}
        
        # Ensure repo exists
        self._ensure_repo_exists()
        
        # Clone/pull
        git = self._clone_or_pull()
        self._git = git
        
        # Copy files
        files_copied = self._copy_files(source_dir)
        
        if not files_copied:
            return {"success": True, "files_copied": 0, "message": "No files to sync"}
        
        # Check for changes
        status = git.status(short=True)
        if not status.strip():
            return {"success": True, "files_copied": files_copied, "message": "No changes"}
        
        # Commit
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        message = commit_message or f"chore: sync knowledge base [{now}]"
        
        git.add(all=True)
        commit_output = git.commit(message)
        logger.info(f"Committed: {message}")
        
        # Push
        push_output = ""
        if push:
            push_output = git.push("origin", self.branch)
            logger.info(f"Pushed to {self.repo}")
        
        return {
            "success": True,
            "files_copied": files_copied,
            "commit_message": message,
            "pushed": push,
        }
    
    def _copy_files(self, source_dir: Path) -> int:
        """
        Copy files from source to clone directory.
        
        Args:
            source_dir: Source directory
            
        Returns:
            Number of files copied
        """
        files_copied = 0
        
        # Preserve repo metadata
        preserve = {".git", ".github"}
        
        for item in source_dir.rglob("*"):
            if item.is_file():
                relative = item.relative_to(source_dir)
                
                # Skip hidden/system files from source
                if any(part.startswith(".") for part in relative.parts):
                    continue
                
                dest = self.clone_dir / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, dest)
                files_copied += 1
        
        logger.debug(f"Copied {files_copied} files")
        return files_copied
