"""
Tests for PAI Shadow Sync utility functions.
"""

import tempfile
from pathlib import Path
import pytest

from coda.shadow import (
    ShadowConfig,
    ShadowSync,
    PAI_DOC_ID,
    get_default_config,
    sync_pai_shadows,
    generate_shadow_summary,
    generate_daily_digest_content,
    generate_weekly_report_content,
    quick_search,
    get_shadow_stats,
)


class TestPAIUtilities:
    """Tests for PAI utility functions."""
    
    def test_pai_doc_id_constant(self):
        """Test PAI_DOC_ID is defined correctly."""
        assert PAI_DOC_ID == "NDxZHneeIw"
    
    def test_get_default_config(self):
        """Test default PAI configuration."""
        config = get_default_config()
        
        assert isinstance(config, ShadowConfig)
        assert PAI_DOC_ID in config.doc_ids
        assert config.sync_interval_hours == 24
        assert config.include_content is True
    
    def test_sync_pai_shadows(self):
        """Test PAI shadow sync with custom dir."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=3,
            )
            
            stats = sync_pai_shadows(config=config, max_pages=3)
            
            assert stats["docs_synced"] == 1
            assert stats["pages_synced"] > 0
            assert stats["errors"] == 0
    
    def test_generate_shadow_summary(self):
        """Test Markdown summary generation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # First sync
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=2,
            )
            ShadowSync(config).run()
            
            # Generate summary
            summary = generate_shadow_summary(Path(tmpdir))
            
            assert "# Coda Shadow Index Summary" in summary
            assert "Total Pages" in summary
            assert PAI_DOC_ID in summary or "PAI" in summary
    
    def test_generate_daily_digest_content(self):
        """Test daily digest HTML generation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # First sync
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=2,
            )
            ShadowSync(config).run()
            
            # Generate daily content
            html = generate_daily_digest_content(Path(tmpdir))
            
            assert "Daily Coda Shadow Digest" in html
            assert "<h3>" in html  # Has HTML structure
            assert "Shadow Index Stats" in html
    
    def test_generate_daily_digest_with_query(self):
        """Test daily digest with search query."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=3,
            )
            ShadowSync(config).run()
            
            html = generate_daily_digest_content(Path(tmpdir), recent_query="coda")
            
            assert "Search:" in html or "coda" in html.lower()
    
    def test_generate_weekly_report_content(self):
        """Test weekly report HTML generation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=2,
            )
            ShadowSync(config).run()
            
            html = generate_weekly_report_content(Path(tmpdir))
            
            assert "Weekly Coda Knowledge Report" in html
            assert "<table" in html  # Has table
            assert "Knowledge Base Overview" in html
    
    def test_get_shadow_stats(self):
        """Test shadow statistics retrieval."""
        # Uses default shadow dir which may or may not exist
        stats = get_shadow_stats()
        
        assert "shadow_dir" in stats
        assert "total_pages" in stats
        assert "total_docs" in stats
        assert "doc_ids" in stats
        assert "docs" in stats
    
    def test_quick_search_with_existing_shadows(self):
        """Test quick search against real shadows."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create shadows first
            config = ShadowConfig(
                shadow_dir=Path(tmpdir),
                doc_ids=[PAI_DOC_ID],
                max_pages_per_doc=3,
            )
            ShadowSync(config).run()
            
            # Override default for test
            from coda.shadow import pai_utils
            original_dir = pai_utils.DEFAULT_SHADOW_DIR
            pai_utils.DEFAULT_SHADOW_DIR = Path(tmpdir)
            
            try:
                results = quick_search("coda")
                assert isinstance(results, list)
            finally:
                pai_utils.DEFAULT_SHADOW_DIR = original_dir
