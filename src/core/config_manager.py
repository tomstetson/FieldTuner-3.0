"""
ConfigManager - Handles BF6 PROFSAVE file parsing and modification.
Merged from V2.0 (bulletproof parsing) and Reborn (comprehensive detection).
"""

import os
import re
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False


class ConfigManager:
    """Manages Battlefield 6 configuration files with bulletproof parsing."""
    
    def __init__(self, config_path: Optional[Path] = None):
        self.config_path: Optional[Path] = None
        self.config_data: Dict[str, str] = {}
        self.original_content: str = ""
        self._raw_lines: List[str] = []
        
        # Auto-detect or use provided path
        if config_path:
            self.config_path = Path(config_path)
        else:
            self._auto_detect_config()
        
        # Load config if path exists
        if self.config_path and self.config_path.exists():
            self.load()
    
    def _get_config_search_paths(self) -> List[Path]:
        """Get all possible BF6 config file locations."""
        paths = []
        home = Path.home()
        
        # OneDrive Documents (priority)
        onedrive_docs = home / "OneDrive" / "Documents"
        if onedrive_docs.exists():
            paths.extend([
                onedrive_docs / "Battlefield 6" / "settings" / "steam" / "PROFSAVE_profile",
                onedrive_docs / "Battlefield 6" / "settings" / "PROFSAVE_profile",
                onedrive_docs / "Battlefield 2042" / "settings" / "steam" / "PROFSAVE_profile",
                onedrive_docs / "Battlefield 2042" / "settings" / "PROFSAVE_profile",
            ])
        
        # Regular Documents
        docs = home / "Documents"
        if docs.exists():
            paths.extend([
                docs / "Battlefield 6" / "settings" / "steam" / "PROFSAVE_profile",
                docs / "Battlefield 6" / "settings" / "PROFSAVE_profile",
                docs / "Battlefield 2042" / "settings" / "steam" / "PROFSAVE_profile",
                docs / "Battlefield 2042" / "settings" / "PROFSAVE_profile",
            ])
        
        # Also check for backup folders with text-format configs
        for base in [onedrive_docs, docs]:
            if base.exists():
                for bf_folder in ["Battlefield 6", "Battlefield 2042"]:
                    settings_dir = base / bf_folder / "settings"
                    if settings_dir.exists():
                        # Look for backup folders
                        for item in settings_dir.iterdir():
                            if item.is_dir() and "backup" in item.name.lower():
                                prof = item / "PROFSAVE_profile"
                                if prof.exists():
                                    paths.append(prof)
                                prof2 = item / "ProfSave_profile"
                                if prof2.exists():
                                    paths.append(prof2)
        
        return paths
    
    def _auto_detect_config(self) -> bool:
        """Auto-detect BF6 config file location."""
        for path in self._get_config_search_paths():
            if path.exists() and self._is_text_format(path):
                self.config_path = path
                return True
        return False
    
    def _is_text_format(self, path: Path) -> bool:
        """Check if file is text format (not binary PROFSAVE)."""
        try:
            with open(path, 'rb') as f:
                header = f.read(100)
                # Binary PROFSAVE starts with "PROFSAVE" magic bytes and has null bytes
                if header.startswith(b'PROFSAVE') or b'\x00' in header:
                    return False
                return True
        except Exception:
            return False
    
    def get_available_configs(self) -> List[Path]:
        """Get all available config files (text format only)."""
        configs = []
        for path in self._get_config_search_paths():
            if path.exists() and self._is_text_format(path):
                configs.append(path)
        return sorted(configs, key=lambda p: p.stat().st_mtime, reverse=True)
    
    def load(self, path: Optional[Path] = None) -> bool:
        """Load config file and parse settings."""
        target = path or self.config_path
        if not target or not target.exists():
            return False
        
        # Check if file is text format
        if not self._is_text_format(target):
            raise ValueError(
                f"Binary PROFSAVE format detected at {target}. "
                "Please use a text-format config from a backup folder."
            )
        
        try:
            self.config_path = target
            content = target.read_text(encoding='utf-8', errors='ignore')
            self.original_content = content
            self._raw_lines = content.splitlines()
            self._parse_config(content)
            return True
        except Exception as e:
            raise RuntimeError(f"Failed to load config: {e}")
    
    def _parse_config(self, content: str):
        """Parse text-format PROFSAVE config."""
        self.config_data.clear()
        
        for line in content.splitlines():
            line = line.strip()
            if not line:
                continue
            
            # Format: "SettingName Value" or "SettingName Value1 Value2 ..."
            parts = line.split(' ', 1)
            if len(parts) >= 2:
                key = parts[0].strip()
                value = parts[1].strip()
                self.config_data[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a setting value."""
        return self.config_data.get(key, default)
    
    def set(self, key: str, value: Any) -> bool:
        """Set a setting value."""
        self.config_data[key] = str(value)
        return True
    
    def update(self, changes: Dict[str, Any]) -> Tuple[bool, str]:
        """Update multiple settings at once."""
        for key, value in changes.items():
            self.set(key, value)
        return True, f"Updated {len(changes)} setting(s)"
    
    def save(self, path: Optional[Path] = None) -> Tuple[bool, str]:
        """Save config back to file, preserving structure."""
        target = path or self.config_path
        if not target:
            return False, "No config path specified"
        
        # Check if game is running
        if self.is_battlefield_running():
            return False, "Battlefield 6 is running. Please close the game first."
        
        try:
            # Build new content preserving original line order
            new_lines = []
            processed_keys = set()
            
            for line in self._raw_lines:
                line_stripped = line.strip()
                if not line_stripped:
                    new_lines.append(line)
                    continue
                
                parts = line_stripped.split(' ', 1)
                if len(parts) >= 1:
                    key = parts[0].strip()
                    if key in self.config_data:
                        new_lines.append(f"{key} {self.config_data[key]}")
                        processed_keys.add(key)
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            
            # Add any new keys not in original file
            for key, value in self.config_data.items():
                if key not in processed_keys:
                    new_lines.append(f"{key} {value}")
            
            # Write to file
            target.write_text('\n'.join(new_lines) + '\n', encoding='utf-8')
            
            # Update original content
            self.original_content = '\n'.join(new_lines) + '\n'
            self._raw_lines = new_lines
            
            return True, f"Saved to {target.name}"
        except Exception as e:
            return False, f"Save failed: {e}"
    
    def is_battlefield_running(self) -> bool:
        """Check if Battlefield 6 is currently running."""
        if not HAS_PSUTIL:
            return False
        
        bf_processes = ['bf6.exe', 'bf2042.exe', 'battlefield6.exe', 'battlefield2042.exe']
        try:
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] and proc.info['name'].lower() in bf_processes:
                    return True
        except Exception:
            pass
        return False
    
    def has_changes(self) -> bool:
        """Check if there are unsaved changes."""
        if not self._raw_lines:
            return False
        
        # Rebuild content and compare
        current_lines = []
        for line in self._raw_lines:
            line_stripped = line.strip()
            if not line_stripped:
                current_lines.append(line)
                continue
            parts = line_stripped.split(' ', 1)
            if len(parts) >= 1:
                key = parts[0].strip()
                if key in self.config_data:
                    current_lines.append(f"{key} {self.config_data[key]}")
                else:
                    current_lines.append(line)
            else:
                current_lines.append(line)
        
        return '\n'.join(current_lines) != '\n'.join(self._raw_lines)
    
    def get_all_settings(self) -> Dict[str, str]:
        """Get all current settings."""
        return self.config_data.copy()
    
    def get_setting_count(self) -> int:
        """Get total number of loaded settings."""
        return len(self.config_data)
    
    def reload(self) -> bool:
        """Reload config from disk, discarding changes."""
        if self.config_path:
            return self.load(self.config_path)
        return False
