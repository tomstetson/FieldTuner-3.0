#!/usr/bin/env python3
"""
FieldTuner Utilities
Common utility functions and helpers
"""

import os
import shutil
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
from datetime import datetime
import logging

try:
    from .constants import AppConstants
    from .debug import log_info, log_error, log_warning
except ImportError:
    # For testing purposes
    from constants import AppConstants
    from debug import log_info, log_error, log_warning

def safe_file_operation(operation_func, *args, **kwargs) -> bool:
    """
    Safely execute file operations with proper error handling
    
    Args:
        operation_func: Function to execute
        *args: Arguments for the function
        **kwargs: Keyword arguments for the function
        
    Returns:
        bool: True if operation succeeded, False otherwise
    """
    try:
        result = operation_func(*args, **kwargs)
        return result is not False
    except FileNotFoundError as e:
        log_error(f"File not found: {e}", "FILE")
        return False
    except PermissionError as e:
        log_error(f"Permission denied: {e}", "FILE")
        return False
    except json.JSONDecodeError as e:
        log_error(f"Invalid JSON: {e}", "FILE")
        return False
    except Exception as e:
        log_error(f"File operation failed: {e}", "FILE")
        return False

def ensure_directory_exists(directory: Path) -> bool:
    """
    Ensure a directory exists, creating it if necessary
    
    Args:
        directory: Path to the directory
        
    Returns:
        bool: True if directory exists or was created successfully
    """
    try:
        directory.mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        log_error(f"Failed to create directory {directory}: {e}", "FILE")
        return False

def safe_json_load(file_path: Path, default: Any = None) -> Any:
    """
    Safely load JSON from a file
    
    Args:
        file_path: Path to the JSON file
        default: Default value to return if loading fails
        
    Returns:
        Loaded JSON data or default value
    """
    try:
        if not file_path.exists():
            return default
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            log_info(f"Loaded JSON from {file_path}", "FILE")
            return data
    except json.JSONDecodeError as e:
        log_error(f"Invalid JSON in {file_path}: {e}", "FILE")
        return default
    except Exception as e:
        log_error(f"Failed to load JSON from {file_path}: {e}", "FILE")
        return default

def safe_json_save(file_path: Path, data: Any) -> bool:
    """
    Safely save data to JSON file
    
    Args:
        file_path: Path to save the JSON file
        data: Data to save
        
    Returns:
        bool: True if save was successful
    """
    try:
        # Ensure directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create backup if file exists
        if file_path.exists():
            backup_path = file_path.with_suffix('.bak')
            shutil.copy2(file_path, backup_path)
        
        # Save JSON
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        log_info(f"Saved JSON to {file_path}", "FILE")
        return True
    except Exception as e:
        log_error(f"Failed to save JSON to {file_path}: {e}", "FILE")
        return False

def validate_setting_value(key: str, value: Any, setting_info: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Validate a setting value against its constraints
    
    Args:
        key: Setting key
        value: Value to validate
        setting_info: Setting metadata
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        setting_type = setting_info.get('type', 'string')
        value_range = setting_info.get('range', [])
        
        if setting_type == 'bool':
            if isinstance(value, bool):
                return True, ""
            elif isinstance(value, (int, str)):
                # Allow conversion from int/str to bool
                try:
                    if isinstance(value, str):
                        bool(value.lower() in ('true', '1', 'yes', 'on'))
                    else:
                        bool(value)
                    return True, ""
                except:
                    return False, f"Value must be boolean for {key}"
            else:
                return False, f"Value must be boolean for {key}"
        
        elif setting_type == 'int':
            try:
                int_value = int(value)
                if value_range and (int_value < value_range[0] or int_value > value_range[1]):
                    return False, f"Value {int_value} out of range {value_range} for {key}"
                return True, ""
            except (ValueError, TypeError):
                return False, f"Value must be integer for {key}"
        
        elif setting_type == 'float':
            try:
                float_value = float(value)
                if value_range and (float_value < value_range[0] or float_value > value_range[1]):
                    return False, f"Value {float_value} out of range {value_range} for {key}"
                return True, ""
            except (ValueError, TypeError):
                return False, f"Value must be float for {key}"
        
        return True, ""
    except Exception as e:
        return False, f"Validation error for {key}: {e}"

def sanitize_setting_value(value: Any, setting_type: str) -> Any:
    """
    Sanitize a setting value to ensure it's the correct type
    
    Args:
        value: Value to sanitize
        setting_type: Expected type
        
    Returns:
        Sanitized value
    """
    try:
        if setting_type == 'bool':
            if isinstance(value, str):
                return value.lower() in ('true', '1', 'yes', 'on')
            return bool(value)
        elif setting_type == 'int':
            return int(float(value))  # Handle "1.0" -> 1
        elif setting_type == 'float':
            return float(value)
        else:
            return str(value)
    except (ValueError, TypeError):
        log_warning(f"Failed to sanitize value {value} as {setting_type}", "VALIDATION")
        return value

def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human-readable format
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted size string
    """
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"

def get_timestamp() -> str:
    """
    Get current timestamp in a consistent format
    
    Returns:
        Timestamp string
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def clean_old_backups(backup_dir: Path, retention_days: int = 30) -> int:
    """
    Clean old backup files
    
    Args:
        backup_dir: Directory containing backups
        retention_days: Number of days to keep backups
        
    Returns:
        Number of files cleaned
    """
    if not backup_dir.exists():
        return 0
    
    cutoff_time = datetime.now().timestamp() - (retention_days * 24 * 60 * 60)
    cleaned_count = 0
    
    try:
        for file_path in backup_dir.glob(f"*{AppConstants.BACKUP_EXTENSION}"):
            if file_path.stat().st_mtime < cutoff_time:
                file_path.unlink()
                cleaned_count += 1
                log_info(f"Cleaned old backup: {file_path.name}", "BACKUP")
    except Exception as e:
        log_error(f"Failed to clean old backups: {e}", "BACKUP")
    
    return cleaned_count

def batch_update_ui(widget, update_func, *args, **kwargs):
    """
    Batch UI updates to reduce redraws
    
    Args:
        widget: Widget to update
        update_func: Function to call for updates
        *args: Arguments for update function
        **kwargs: Keyword arguments for update function
    """
    widget.setUpdatesEnabled(False)
    try:
        update_func(*args, **kwargs)
    finally:
        widget.setUpdatesEnabled(True)

def create_backup_filename(name: str, extension: str = AppConstants.BACKUP_EXTENSION) -> str:
    """
    Create a backup filename with timestamp
    
    Args:
        name: Base name for the backup
        extension: File extension
        
    Returns:
        Backup filename
    """
    timestamp = get_timestamp()
    return f"{name}_{timestamp}{extension}"

def is_valid_config_file(file_path: Path) -> bool:
    """
    Check if a file is a valid BF6 config file
    
    Args:
        file_path: Path to check
        
    Returns:
        True if file appears to be a valid config
    """
    if not file_path.exists():
        return False
    
    try:
        # Check file size (should be reasonable for a config file)
        file_size = file_path.stat().st_size
        if file_size < 100 or file_size > 10 * 1024 * 1024:  # 100 bytes to 10MB
            return False
        
        # Check if file is readable
        with open(file_path, 'rb') as f:
            # Read first few bytes to check if it's binary
            first_bytes = f.read(100)
            if not first_bytes:
                return False
        
        return True
    except Exception:
        return False

def get_system_info() -> Dict[str, Any]:
    """
    Get system information for debugging
    
    Returns:
        Dictionary with system information
    """
    import platform
    import sys
    
    return {
        'python_version': sys.version,
        'platform': platform.platform(),
        'architecture': platform.architecture(),
        'processor': platform.processor(),
        'working_directory': str(Path.cwd()),
        'user_home': str(Path.home()),
        'app_data_dir': str(AppConstants.USER_DATA_DIR)
    }
