"""
Shadow Sync Configuration

Configuration dataclass and defaults for the shadow sync engine.
"""

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional
import json

logger = logging.getLogger(__name__)

# Default shadow directory location
DEFAULT_SHADOW_DIR = Path.home() / ".pai" / "coda_shadows"


@dataclass
class ShadowConfig:
    """
    Configuration for the Coda Shadow Sync engine.
    
    Attributes:
        shadow_dir: Local directory for shadow files
        doc_ids: List of Coda doc IDs to sync
        sync_interval_hours: Hours between automatic re-syncs
        include_content: Whether to include page content (not just metadata)
        generate_synopses: Whether to generate LLM synopses (requires content)
        max_pages_per_doc: Maximum pages to sync per document
    """
    shadow_dir: Path = field(default_factory=lambda: DEFAULT_SHADOW_DIR)
    doc_ids: List[str] = field(default_factory=list)
    sync_interval_hours: int = 24
    include_content: bool = True
    generate_synopses: bool = False  # Requires LLM integration
    max_pages_per_doc: int = 100
    
    def __post_init__(self):
        """Ensure shadow_dir is a Path object."""
        if isinstance(self.shadow_dir, str):
            self.shadow_dir = Path(self.shadow_dir)
    
    @classmethod
    def from_file(cls, config_path: Path) -> "ShadowConfig":
        """
        Load configuration from a JSON file.
        
        Args:
            config_path: Path to config.json
            
        Returns:
            ShadowConfig instance
        """
        logger.info(f"Loading shadow config from {config_path}")
        with open(config_path, "r") as f:
            data = json.load(f)
        
        # Convert shadow_dir to Path if present
        if "shadow_dir" in data:
            data["shadow_dir"] = Path(data["shadow_dir"])
        
        return cls(**data)
    
    def save(self, config_path: Optional[Path] = None) -> Path:
        """
        Save configuration to a JSON file.
        
        Args:
            config_path: Path to save to (default: shadow_dir/config.json)
            
        Returns:
            Path to saved config file
        """
        if config_path is None:
            config_path = self.shadow_dir / "config.json"
        
        self.shadow_dir.mkdir(parents=True, exist_ok=True)
        
        data = {
            "shadow_dir": str(self.shadow_dir),
            "doc_ids": self.doc_ids,
            "sync_interval_hours": self.sync_interval_hours,
            "include_content": self.include_content,
            "generate_synopses": self.generate_synopses,
            "max_pages_per_doc": self.max_pages_per_doc,
        }
        
        with open(config_path, "w") as f:
            json.dump(data, f, indent=2)
        
        logger.info(f"Saved shadow config to {config_path}")
        return config_path
    
    def add_doc(self, doc_id: str) -> None:
        """Add a doc ID to the sync list."""
        if doc_id not in self.doc_ids:
            self.doc_ids.append(doc_id)
            logger.info(f"Added doc {doc_id} to shadow config")
    
    def remove_doc(self, doc_id: str) -> None:
        """Remove a doc ID from the sync list."""
        if doc_id in self.doc_ids:
            self.doc_ids.remove(doc_id)
            logger.info(f"Removed doc {doc_id} from shadow config")
