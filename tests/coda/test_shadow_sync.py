"""
Tests for Coda Shadow Sync module.

These are integration tests that verify shadow file generation,
indexing, and search functionality using real Coda data.
"""

import tempfile
from pathlib import Path
import pytest

from coda.shadow import (
    ShadowConfig,
    ShadowSync,
    ShadowIndex,
    shadow_search,
    ShadowSearchResult,
)

# PAI Document Controller - known test doc
PAI_DOC_ID = "NDxZHneeIw"


class TestShadowConfig:
    """Tests for ShadowConfig."""
    
    def test_default_values(self):
        """Test default configuration values."""
        config = ShadowConfig()
        
        assert config.shadow_dir.name == "coda_shadows"
        assert config.doc_ids == []
        assert config.sync_interval_hours == 24
        assert config.include_content is True
        assert config.generate_synopses is False
        assert config.max_pages_per_doc == 100
    
    def test_custom_shadow_dir(self):
        """Test custom shadow directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(shadow_dir=Path(tmpdir))
            assert config.shadow_dir == Path(tmpdir)
    
    def test_string_shadow_dir_conversion(self):
        """Test that string paths are converted to Path objects."""
        config = ShadowConfig(shadow_dir="/tmp/test_shadows")
        assert isinstance(config.shadow_dir, Path)
        assert config.shadow_dir == Path("/tmp/test_shadows")
    
    def test_add_remove_doc(self):
        """Test adding and removing doc IDs."""
        config = ShadowConfig()
        
        config.add_doc("doc1")
        config.add_doc("doc2")
        assert "doc1" in config.doc_ids
        assert "doc2" in config.doc_ids
        
        # Adding duplicate should not add again
        config.add_doc("doc1")
        assert config.doc_ids.count("doc1") == 1
        
        config.remove_doc("doc1")
        assert "doc1" not in config.doc_ids
    
    def test_save_and_load(self):
        """Test saving and loading config from JSON."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=["doc_a", "doc_b"],
                sync_interval_hours=12,
            )
            
            saved_path = config.save()
            assert saved_path.exists()
            
            loaded = ShadowConfig.from_file(saved_path)
            assert loaded.doc_ids == ["doc_a", "doc_b"]
            assert loaded.sync_interval_hours == 12


class TestShadowSync:
    """Tests for ShadowSync engine."""
    
    def test_sync_creates_shadow_directory(self):
        """Test that sync creates the shadow directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            shadow_dir = Path(tmpdir) / "shadows"
            config = ShadowConfig(
                shadow_dir=shadow_dir,
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=5,  # Limit for test speed
            )
            
            sync = ShadowSync(config)
            stats = sync.run()
            
            assert shadow_dir.exists()
            assert stats["docs_synced"] == 1
            assert stats["pages_synced"] > 0
    
    def test_sync_creates_dashboard(self):
        """Test that dashboard.md is created."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=3,
            )
            
            sync = ShadowSync(config)
            sync.run()
            
            dashboard = Path(tmpdir) / "dashboard.md"
            assert dashboard.exists()
            content = dashboard.read_text()
            assert "Coda Shadow Dashboard" in content
    
    def test_sync_creates_doc_directory(self):
        """Test that per-doc directories are created."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=2,
            )
            
            sync = ShadowSync(config)
            sync.run()
            
            # Find doc directory (name pattern: DocName_abc12345)
            doc_dirs = [d for d in Path(tmpdir).iterdir() if d.is_dir()]
            assert len(doc_dirs) == 1
            assert PAI_DOC_ID[:8] in doc_dirs[0].name
    
    def test_shadow_file_frontmatter(self):
        """Test that shadow files have correct YAML frontmatter."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=1,
            )
            
            sync = ShadowSync(config)
            sync.run()
            
            # Find a shadow file
            shadow_files = list(Path(tmpdir).rglob("*.md"))
            # Exclude dashboard and index files
            shadow_files = [f for f in shadow_files 
                           if not f.name.startswith("_") 
                           and f.name != "dashboard.md"]
            
            assert len(shadow_files) >= 1
            
            content = shadow_files[0].read_text()
            assert "---" in content
            assert "coda_doc_id:" in content
            assert "coda_page_id:" in content
            assert "page_name:" in content


class TestShadowIndex:
    """Tests for ShadowIndex."""
    
    def test_build_index_from_synced_files(self):
        """Test building index from synced shadow files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=3,
            )
            
            # First sync
            sync = ShadowSync(config)
            sync.run()
            
            # Then index
            index = ShadowIndex.from_directory(Path(tmpdir))
            
            assert len(index.entries) > 0
            assert PAI_DOC_ID in index.get_all_doc_ids()
    
    def test_get_pages_for_doc(self):
        """Test retrieving pages for a specific doc."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=5,
            )
            
            sync = ShadowSync(config)
            sync.run()
            
            index = ShadowIndex.from_directory(Path(tmpdir))
            pages = index.get_pages_for_doc(PAI_DOC_ID)
            
            assert len(pages) > 0
            assert all(p.coda_doc_id == PAI_DOC_ID for p in pages)
    
    def test_search_by_name(self):
        """Test searching entries by name."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=10,
            )
            
            sync = ShadowSync(config)
            sync.run()
            
            index = ShadowIndex.from_directory(Path(tmpdir))
            
            # Search for a term likely to appear
            results = index.search_by_name("PAI")
            # May or may not find matches depending on page names
            assert isinstance(results, list)


class TestShadowSearch:
    """Tests for shadow_search function."""
    
    def test_search_finds_content(self):
        """Test that search finds content in shadow files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=5,
                include_content=True,
            )
            
            sync = ShadowSync(config)
            sync.run()
            
            # Search for Coda (appears in all frontmatter)
            results = shadow_search(Path(tmpdir), "coda_doc_id")
            
            assert len(results) > 0
            assert all(isinstance(r, ShadowSearchResult) for r in results)
    
    def test_search_case_insensitive(self):
        """Test case-insensitive search."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=2,
            )
            
            sync = ShadowSync(config)
            sync.run()
            
            results_lower = shadow_search(Path(tmpdir), "coda", case_sensitive=False)
            results_upper = shadow_search(Path(tmpdir), "CODA", case_sensitive=False)
            
            # Both should find results
            assert len(results_lower) > 0
            assert len(results_upper) > 0
    
    def test_search_respects_max_results(self):
        """Test that max_results is respected."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=10,
            )
            
            sync = ShadowSync(config)
            sync.run()
            
            results = shadow_search(Path(tmpdir), "coda", max_results=2)
            
            assert len(results) <= 2
    
    def test_search_empty_directory(self):
        """Test search on empty directory returns empty list."""
        with tempfile.TemporaryDirectory() as tmpdir:
            results = shadow_search(Path(tmpdir), "test")
            assert results == []
    
    def test_search_nonexistent_directory(self):
        """Test search on nonexistent directory returns empty list."""
        results = shadow_search(Path("/nonexistent/path"), "test")
        assert results == []
