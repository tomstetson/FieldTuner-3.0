"""
BackupManager - Handles config file backups with metadata.
Merged from V2.0 and Reborn for comprehensive backup functionality.
"""

import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional


class BackupManager:
    """Manages configuration file backups with metadata and restore functionality."""
    
    def __init__(self, backup_dir: Optional[Path] = None):
        if backup_dir:
            self.backup_dir = Path(backup_dir)
        else:
            # Default to AppData
            self.backup_dir = Path.home() / "AppData" / "Roaming" / "FieldTuner" / "backups"
        
        self.backup_dir.mkdir(parents=True, exist_ok=True)
    
    def create_backup(self, config_path: Path, description: str = "") -> Optional[Path]:
        """Create a timestamped backup of the config file."""
        if not config_path or not config_path.exists():
            return None
        
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_name = f"backup_{timestamp}"
            if description:
                # Sanitize description for filename
                safe_desc = "".join(c if c.isalnum() or c in '-_' else '_' for c in description)
                backup_name = f"{backup_name}_{safe_desc[:30]}"
            
            backup_path = self.backup_dir / backup_name
            backup_path.mkdir(parents=True, exist_ok=True)
            
            # Copy config file
            config_backup = backup_path / config_path.name
            shutil.copy2(config_path, config_backup)
            
            # Save metadata
            metadata = {
                'timestamp': timestamp,
                'datetime': datetime.now().isoformat(),
                'description': description,
                'original_path': str(config_path),
                'file_name': config_path.name,
                'file_size': config_path.stat().st_size
            }
            
            metadata_file = backup_path / 'metadata.json'
            with open(metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            return backup_path
        except Exception as e:
            print(f"Backup failed: {e}")
            return None
    
    def get_backups(self) -> List[Dict]:
        """Get list of all available backups with metadata."""
        backups = []
        
        try:
            for item in sorted(self.backup_dir.iterdir(), reverse=True):
                if item.is_dir():
                    metadata_file = item / 'metadata.json'
                    if metadata_file.exists():
                        with open(metadata_file, 'r') as f:
                            metadata = json.load(f)
                        backups.append({
                            'name': item.name,
                            'path': item,
                            'metadata': metadata
                        })
                    else:
                        # Backup without metadata
                        backups.append({
                            'name': item.name,
                            'path': item,
                            'metadata': {
                                'timestamp': item.name.split('_')[1] if '_' in item.name else 'Unknown',
                                'description': 'No metadata'
                            }
                        })
        except Exception as e:
            print(f"Error reading backups: {e}")
        
        return backups
    
    def restore_backup(self, backup_name: str, target_path: Path) -> tuple[bool, str]:
        """Restore a backup to the specified target path."""
        try:
            backup_path = self.backup_dir / backup_name
            
            if not backup_path.exists():
                return False, f"Backup not found: {backup_name}"
            
            # Find config file in backup
            config_files = [f for f in backup_path.iterdir() 
                          if f.is_file() and f.name != 'metadata.json']
            
            if not config_files:
                return False, "No config file found in backup"
            
            # Create backup of current file before restoring
            if target_path.exists():
                self.create_backup(target_path, f"before_restore_{backup_name}")
            
            # Restore
            shutil.copy2(config_files[0], target_path)
            
            return True, f"Restored from {backup_name}"
        except Exception as e:
            return False, f"Restore failed: {e}"
    
    def delete_backup(self, backup_name: str) -> tuple[bool, str]:
        """Delete a backup."""
        try:
            backup_path = self.backup_dir / backup_name
            
            if not backup_path.exists():
                return False, f"Backup not found: {backup_name}"
            
            shutil.rmtree(backup_path)
            return True, f"Deleted {backup_name}"
        except Exception as e:
            return False, f"Delete failed: {e}"
    
    def get_backup_count(self) -> int:
        """Get total number of backups."""
        return len(self.get_backups())
    
    def cleanup_old_backups(self, keep_count: int = 20):
        """Remove old backups, keeping only the most recent ones."""
        backups = self.get_backups()
        
        if len(backups) <= keep_count:
            return
        
        # Delete oldest backups
        for backup in backups[keep_count:]:
            self.delete_backup(backup['name'])
