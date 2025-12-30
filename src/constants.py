#!/usr/bin/env python3
"""
FieldTuner Constants
Application-wide constants and configuration values
"""

from pathlib import Path
from typing import List, Dict, Any

class AppConstants:
    """Application constants"""
    
    # Application Info
    APP_NAME = "FieldTuner"
    APP_VERSION = "1.0.0"
    APP_AUTHOR = "Tom Stetson"
    APP_DESCRIPTION = "Battlefield 6 Configuration Tool"
    
    # Window Configuration
    WINDOW_TITLE = "FieldTuner - Battlefield 6 Configuration Tool"
    WINDOW_MIN_WIDTH = 1200
    WINDOW_MIN_HEIGHT = 800
    WINDOW_DEFAULT_WIDTH = 1400
    WINDOW_DEFAULT_HEIGHT = 900
    WINDOW_MAX_WIDTH = 2000
    WINDOW_MAX_HEIGHT = 1400
    
    # File Paths
    USER_DATA_DIR = Path.home() / "AppData" / "Roaming" / "FieldTuner"
    BACKUP_DIR = USER_DATA_DIR / "backups"
    LOGS_DIR = USER_DATA_DIR / "logs"
    FAVORITES_FILE = USER_DATA_DIR / "favorites.json"
    
    # Battlefield 6 Config Paths
    BF6_CONFIG_PATHS = [
        Path.home() / "Documents" / "Battlefield 6" / "settings" / "steam" / "PROFSAVE_profile",
        Path.home() / "Documents" / "Battlefield 6" / "settings" / "PROFSAVE_profile",
        Path.home() / "OneDrive" / "Documents" / "Battlefield 6" / "settings" / "steam" / "PROFSAVE_profile",
        Path.home() / "OneDrive" / "Documents" / "Battlefield 6" / "settings" / "PROFSAVE_profile"
    ]
    
    # UI Constants
    TAB_SPACING = 12
    WIDGET_MARGIN = 16
    BUTTON_HEIGHT = 32
    TOGGLE_SWITCH_WIDTH = 52
    TOGGLE_SWITCH_HEIGHT = 28
    
    # Performance Settings
    MAX_LOG_BUFFER_SIZE = 1000
    UI_UPDATE_BATCH_SIZE = 10
    BACKUP_RETENTION_DAYS = 30
    
    # Setting Categories
    SETTING_CATEGORIES = [
        "Graphics API",
        "Display",
        "Performance", 
        "Graphics Quality",
        "Advanced Graphics",
        "Ray Tracing",
        "Upscaling",
        "Competitive",
        "Audio",
        "Input"
    ]
    
    # Preset Names
    PRESET_NAMES = {
        'esports_pro': 'Esports Pro',
        'competitive': 'Competitive',
        'balanced': 'Balanced',
        'quality': 'Quality',
        'performance': 'Performance'
    }
    
    # Color Scheme
    COLORS = {
        'primary': '#2a2a2a',
        'secondary': '#333333',
        'accent': '#4a90e2',
        'success': '#4caf50',
        'warning': '#ff9800',
        'error': '#f44336',
        'text': '#ffffff',
        'text_secondary': '#cccccc'
    }
    
    # Logging
    LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR']
    LOG_CATEGORIES = ['MAIN', 'CONFIG', 'UI', 'BACKUP', 'FAVORITES', 'GENERAL']
    
    # File Extensions
    BACKUP_EXTENSION = '.bak'
    LOG_EXTENSION = '.log'
    JSON_EXTENSION = '.json'
    
    # Validation
    MAX_SETTING_VALUE_LENGTH = 1000
    MIN_FPS_LIMIT = 30
    MAX_FPS_LIMIT = 500
    MIN_FOV = 60
    MAX_FOV = 120
    
    # Error Messages
    ERROR_MESSAGES = {
        'config_not_found': 'No Battlefield 6 config file found - Please check your game installation',
        'permission_denied': 'Permission denied - Please run as administrator',
        'file_corrupted': 'Config file appears to be corrupted',
        'backup_failed': 'Failed to create backup',
        'save_failed': 'Failed to save configuration changes',
        'load_failed': 'Failed to load configuration'
    }
    
    # Success Messages
    SUCCESS_MESSAGES = {
        'config_loaded': 'Configuration loaded successfully',
        'changes_applied': 'Changes applied successfully',
        'backup_created': 'Backup created successfully',
        'settings_saved': 'Settings saved successfully'
    }
