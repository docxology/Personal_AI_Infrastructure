"""
Mirror Configuration

Configuration dataclass for triple mirror sync.
"""

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# Default paths and IDs
DEFAULT_SOURCE_DIR = Path.home() / ".pai" / "knowledge"
DEFAULT_CODA_DOC_ID = "NDxZHneeIw"  # PAI Document Controller
DEFAULT_GITHUB_REPO = "GithubBlanket/pai-knowledge"
DEFAULT_GITHUB_BRANCH = "main"


@dataclass
class MirrorConfig:
    """
    Configuration for triple mirror sync.
    
    Attributes:
        source_dir: Local knowledge base directory to mirror
        coda_doc_id: Coda document ID to sync pages to
        github_repo: GitHub repository (owner/name format)
        github_branch: Git branch for commits
        drive_folder_id: Google Drive folder ID (None = root)
        enable_coda: Enable Coda mirror
        enable_github: Enable GitHub mirror
        enable_drive: Enable Drive mirror
        auto_commit_message: Default commit message template
    """
    source_dir: Path = field(default_factory=lambda: DEFAULT_SOURCE_DIR)
    coda_doc_id: str = DEFAULT_CODA_DOC_ID
    github_repo: str = DEFAULT_GITHUB_REPO
    github_branch: str = DEFAULT_GITHUB_BRANCH
    drive_folder_id: Optional[str] = None
    enable_coda: bool = True
    enable_github: bool = True
    enable_drive: bool = True
    auto_commit_message: str = "chore: sync knowledge base [mirror]"
    
    def __post_init__(self):
        """Ensure source_dir is a Path object."""
        if isinstance(self.source_dir, str):
            self.source_dir = Path(self.source_dir)
    
    @classmethod
    def from_file(cls, config_path: Path) -> "MirrorConfig":
        """
        Load configuration from JSON file.
        
        Args:
            config_path: Path to config.json
            
        Returns:
            MirrorConfig instance
        """
        logger.info(f"Loading mirror config from {config_path}")
        with open(config_path, "r") as f:
            data = json.load(f)
        
        if "source_dir" in data:
            data["source_dir"] = Path(data["source_dir"])
        
        return cls(**data)
    
    def save(self, config_path: Optional[Path] = None) -> Path:
        """
        Save configuration to JSON file.
        
        Args:
            config_path: Path to save (default: source_dir/mirror_config.json)
            
        Returns:
            Path to saved file
        """
        if config_path is None:
            config_path = self.source_dir / "mirror_config.json"
        
        self.source_dir.mkdir(parents=True, exist_ok=True)
        
        data = {
            "source_dir": str(self.source_dir),
            "coda_doc_id": self.coda_doc_id,
            "github_repo": self.github_repo,
            "github_branch": self.github_branch,
            "drive_folder_id": self.drive_folder_id,
            "enable_coda": self.enable_coda,
            "enable_github": self.enable_github,
            "enable_drive": self.enable_drive,
            "auto_commit_message": self.auto_commit_message,
        }
        
        with open(config_path, "w") as f:
            json.dump(data, f, indent=2)
        
        logger.info(f"Saved mirror config to {config_path}")
        return config_path
    
    def validate(self) -> bool:
        """
        Validate configuration.
        
        Returns:
            True if valid
            
        Raises:
            ValueError: If invalid
        """
        if not self.source_dir.exists():
            logger.warning(f"Source directory does not exist: {self.source_dir}")
        
        if self.enable_github and "/" not in self.github_repo:
            raise ValueError(f"Invalid github_repo format: {self.github_repo} (expected owner/name)")
        
        return True


def get_default_config() -> MirrorConfig:
    """
    Get default PAI mirror configuration.
    
    Returns:
        MirrorConfig with PAI defaults
    """
    return MirrorConfig(
        source_dir=DEFAULT_SOURCE_DIR,
        coda_doc_id=DEFAULT_CODA_DOC_ID,
        github_repo=DEFAULT_GITHUB_REPO,
    )
