"""
Basic tests for FieldTuner to ensure the application can start and basic functionality works.
"""

import pytest
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def test_imports():
    """Test that we can import the main modules."""
    try:
        from constants import AppConstants
        from utils import safe_file_operation, safe_json_load, safe_json_save
        from debug import log_info, log_error
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import modules: {e}")

def test_constants():
    """Test that constants are properly defined."""
    from constants import AppConstants
    
    assert hasattr(AppConstants, 'WINDOW_TITLE')
    assert hasattr(AppConstants, 'WINDOW_MIN_WIDTH')
    assert hasattr(AppConstants, 'WINDOW_MIN_HEIGHT')
    assert hasattr(AppConstants, 'USER_DATA_DIR')
    assert hasattr(AppConstants, 'BF6_CONFIG_PATHS')
    
    assert AppConstants.WINDOW_MIN_WIDTH > 0
    assert AppConstants.WINDOW_MIN_HEIGHT > 0
    assert len(AppConstants.BF6_CONFIG_PATHS) > 0

def test_utils():
    """Test that utility functions work."""
    from utils import format_file_size, get_timestamp
    
    # Test file size formatting
    assert format_file_size(1024) == "1.00 KB"
    assert format_file_size(1024 * 1024) == "1.00 MB"
    assert format_file_size(1024 * 1024 * 1024) == "1.00 GB"
    
    # Test timestamp generation
    timestamp = get_timestamp()
    assert len(timestamp) > 0
    assert isinstance(timestamp, str)

def test_app_can_start():
    """Test that the main application can be imported without errors."""
    try:
        # This will test if the main module can be imported
        # We don't actually create the QApplication to avoid GUI issues in CI
        import main
        assert True
    except Exception as e:
        pytest.fail(f"Failed to import main module: {e}")

if __name__ == "__main__":
    pytest.main([__file__])
