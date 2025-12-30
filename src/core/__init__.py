"""Core module for FieldTuner Ultimate"""
from .config_manager import ConfigManager
from .settings_database import SETTINGS_DATABASE, get_setting_info, search_settings
from .backup_manager import BackupManager
from .presets import PRESETS, apply_preset

__all__ = [
    'ConfigManager',
    'SETTINGS_DATABASE',
    'get_setting_info',
    'search_settings',
    'BackupManager',
    'PRESETS',
    'apply_preset',
]
