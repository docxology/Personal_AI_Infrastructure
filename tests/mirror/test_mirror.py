"""
Tests for Triple Mirror module.

Integration tests for Coda, GitHub, and Drive mirrors.
"""

import tempfile
from pathlib import Path
import pytest

from mirror import (
    MirrorConfig,
    get_default_config,
    MirrorSync,
    SyncResult,
    CodaMirror,
    GitHubMirror,
    DriveMirror,
)

# Test constants
PAI_DOC_ID = "NDxZHneeIw"
TEST_GITHUB_REPO = "GithubBlanket/pai-knowledge"


class TestMirrorConfig:
    """Tests for MirrorConfig."""
    
    def test_default_values(self):
        """Test default configuration values."""
        config = MirrorConfig()
        
        assert config.coda_doc_id == PAI_DOC_ID
        assert config.github_repo == TEST_GITHUB_REPO
        assert config.github_branch == "main"
        assert config.enable_coda is True
        assert config.enable_github is True
        assert config.enable_drive is True
    
    def test_get_default_config(self):
        """Test get_default_config helper."""
        config = get_default_config()
        
        assert isinstance(config, MirrorConfig)
        assert config.coda_doc_id == PAI_DOC_ID
    
    def test_string_source_dir_conversion(self):
        """Test string paths are converted to Path."""
        config = MirrorConfig(source_dir="/tmp/test")
        assert isinstance(config.source_dir, Path)
    
    def test_validate_github_repo_format(self):
        """Test validation of github_repo format."""
        config = MirrorConfig(github_repo="GithubBlanket/repo")
        assert config.validate() is True
        
        bad_config = MirrorConfig(github_repo="invalid-format")
        with pytest.raises(ValueError):
            bad_config.validate()
    
    def test_save_and_load(self):
        """Test saving and loading config."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = MirrorConfig(
                source_dir=Path(tmpdir),
                coda_doc_id="test123",
                github_repo="test/repo",
            )
            
            saved = config.save()
            assert saved.exists()
            
            loaded = MirrorConfig.from_file(saved)
            assert loaded.coda_doc_id == "test123"
            assert loaded.github_repo == "test/repo"


class TestMirrorSync:
    """Tests for MirrorSync orchestrator."""
    
    def test_get_status(self):
        """Test status reporting."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = MirrorConfig(source_dir=Path(tmpdir))
            sync = MirrorSync(config)
            
            status = sync.get_status()
            
            assert "source_dir" in status
            assert "targets" in status
            assert "coda" in status["targets"]
            assert "github" in status["targets"]
            assert "drive" in status["targets"]
    
    def test_sync_result_structure(self):
        """Test SyncResult dataclass."""
        result = SyncResult(
            target="test",
            success=True,
            stats={"files": 10},
            elapsed_seconds=1.5
        )
        
        assert result.target == "test"
        assert result.success is True
        assert result.stats["files"] == 10
        assert result.error is None


class TestCodaMirror:
    """Tests for CodaMirror."""
    
    def test_init(self):
        """Test CodaMirror initialization."""
        mirror = CodaMirror(doc_id=PAI_DOC_ID)
        assert mirror.doc_id == PAI_DOC_ID
    
    def test_sync_nonexistent_source(self):
        """Test sync with nonexistent source."""
        mirror = CodaMirror()
        result = mirror.sync(Path("/nonexistent/path"))
        
        assert result["success"] is False
        assert "error" in result
    
    def test_sync_with_real_source(self):
        """Test sync with real source directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test files
            source = Path(tmpdir)
            (source / "test.md").write_text("# Test\n\nTest content")
            (source / "readme.md").write_text("# README\n\nDoc content")
            
            mirror = CodaMirror(doc_id=PAI_DOC_ID)
            result = mirror.sync(source)
            
            assert result["success"] is True
            assert result["pages_created"] + result["pages_updated"] >= 0


class TestGitHubMirror:
    """Tests for GitHubMirror."""
    
    def test_init(self):
        """Test GitHubMirror initialization."""
        mirror = GitHubMirror(repo=TEST_GITHUB_REPO)
        assert mirror.owner == "GithubBlanket"
        assert mirror.repo_name == "pai-knowledge"
    
    def test_sync_nonexistent_source(self):
        """Test sync with nonexistent source."""
        mirror = GitHubMirror(repo=TEST_GITHUB_REPO)
        result = mirror.sync(Path("/nonexistent/path"))
        
        assert result["success"] is False


class TestDriveMirror:
    """Tests for DriveMirror."""
    
    def test_init(self):
        """Test DriveMirror initialization."""
        mirror = DriveMirror(folder_id="test123")
        assert mirror.folder_id == "test123"
    
    def test_sync_nonexistent_source(self):
        """Test sync with nonexistent source."""
        mirror = DriveMirror()
        result = mirror.sync(Path("/nonexistent/path"))
        
        assert result["success"] is False
        assert "error" in result
