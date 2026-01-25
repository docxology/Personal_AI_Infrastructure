"""
Triple Mirror Module

Syncs PAI knowledge bases to multiple backends:
- Coda (Document pages)
- GitHub (Version-controlled repository)
- Google Drive (Cloud files)
"""

from mirror.mirror_config import MirrorConfig, get_default_config
from mirror.mirror_sync import MirrorSync, SyncResult
from mirror.mirror_coda import CodaMirror
from mirror.mirror_github import GitHubMirror
from mirror.mirror_drive import DriveMirror

__all__ = [
    "MirrorConfig",
    "get_default_config",
    "MirrorSync",
    "SyncResult",
    "CodaMirror",
    "GitHubMirror",
    "DriveMirror",
]

__version__ = "1.0.0"
