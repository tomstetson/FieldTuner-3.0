"""Quick test script for FieldTuner Ultimate"""
import sys
sys.path.insert(0, 'src')

from core.settings_database import SETTINGS_DATABASE, search_settings, get_categories
from core.presets import PRESETS, get_preset_names
from core.config_manager import ConfigManager
from core.backup_manager import BackupManager

print("=" * 60)
print("FieldTuner Ultimate - Component Test")
print("=" * 60)

# Test settings database
print(f"\n✅ Settings Database: {len(SETTINGS_DATABASE)} settings")
print(f"   Categories: {get_categories()}")

# Test search
fps_results = search_settings("fps")
blur_results = search_settings("blur")
mouse_results = search_settings("mouse")
print(f"\n✅ Search Tests:")
print(f"   'fps' → {len(fps_results)} results")
print(f"   'blur' → {len(blur_results)} results")
print(f"   'mouse' → {len(mouse_results)} results")

# Test presets
print(f"\n✅ Presets: {len(PRESETS)}")
for name in get_preset_names():
    preset = PRESETS[name]
    print(f"   {preset['icon']} {preset['name']}: {len(preset['settings'])} settings")

# Test config manager
print(f"\n✅ Config Manager:")
cm = ConfigManager()
configs = cm.get_available_configs()
print(f"   Available configs: {len(configs)}")
for c in configs[:3]:
    print(f"   - {c}")

if cm.config_path:
    print(f"   Active config: {cm.config_path.name}")
    print(f"   Settings loaded: {cm.get_setting_count()}")

# Test backup manager
print(f"\n✅ Backup Manager:")
bm = BackupManager()
backups = bm.get_backups()
print(f"   Backup directory: {bm.backup_dir}")
print(f"   Existing backups: {len(backups)}")

print("\n" + "=" * 60)
print("All components loaded successfully!")
print("=" * 60)
