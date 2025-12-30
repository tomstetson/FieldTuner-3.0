# 🎮 FieldTuner 3.0

**The definitive Battlefield 6 configuration tool - Consolidated from V1.0, V2.0, and Max**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyQt6](https://img.shields.io/badge/PyQt6-6.5+-green.svg)](https://pypi.org/project/PyQt6/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ✨ Features

### 🎯 Core Features
- **Auto-detect config files** - Finds BF6 settings automatically (OneDrive & regular Documents)
- **100+ documented settings** - Comprehensive database with tooltips and search aliases
- **Smart search** - Natural language search ("fps", "blur", "vsync", etc.)
- **5 optimized presets** - Esports Pro, Competitive, Balanced, Quality, Ultra
- **Bulletproof backups** - Automatic backups with metadata and easy restore

### 🖥️ Modern UI
- **Dark theme** - Professional, eye-friendly interface
- **Tabbed layout** - Organized by category (Graphics, Performance, Audio, Input)
- **Dashboard** - Quick overview and one-click preset application
- **Status cards** - See config status, settings count, and backup count at a glance

### 🛡️ Safety Features
- **Game running detection** - Prevents editing while BF6 is running
- **Binary format detection** - Only loads editable text-format configs
- **Auto-backup on start** - Always have a restore point
- **Backup before save** - Never lose your settings

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Battlefield 6 installed and run at least once

### Installation

```bash
# Navigate to the project
cd FieldTuner-3.0

# Install dependencies
pip install -r requirements.txt

# Run the application
python src/main.py
```

---

## 📁 Project Structure

```
FieldTuner-3.0/
├── src/
│   ├── core/
│   │   ├── config_manager.py    # Config file handling
│   │   ├── settings_database.py # 100+ settings with metadata
│   │   ├── backup_manager.py    # Backup/restore functionality
│   │   └── presets.py           # Optimized presets
│   ├── ui/
│   │   ├── main_window.py       # Main application window
│   │   └── theme.py             # Dark theme styling
│   └── main.py                  # Entry point
├── config/                      # Configuration files
├── assets/                      # Icons and images
├── tests/                       # Test suite
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 🎮 Presets

| Preset | Description | Use Case |
|--------|-------------|----------|
| **🏆 Esports Pro** | Maximum FPS, lowest settings | Competitive tournaments |
| **🎯 Competitive** | Good FPS with acceptable visuals | Ranked play |
| **⚖️ Balanced** | Mix of performance and quality | Most players |
| **✨ Quality** | High visuals, still playable | Single-player |
| **💎 Ultra Quality** | Maximum eye candy | Screenshots, high-end PCs |

---

## 🔍 Search Examples

The search feature understands natural language:

- `"fps"` → Frame rate settings
- `"blur"` → Motion blur settings
- `"mouse"` → Mouse sensitivity settings
- `"vsync"` → V-Sync settings
- `"shadows"` → Shadow quality
- `"reflex"` → NVIDIA Reflex low latency

---

## 📍 Config File Locations

FieldTuner Ultimate automatically searches:

- `Documents/Battlefield 6/settings/steam/PROFSAVE_profile`
- `Documents/Battlefield 6/settings/PROFSAVE_profile`
- `OneDrive/Documents/Battlefield 6/settings/steam/PROFSAVE_profile`
- `OneDrive/Documents/Battlefield 6/settings/PROFSAVE_profile`
- Backup folders with text-format configs

---

## 💾 Backups

Backups are stored in: `%APPDATA%/FieldTuner/backups/`

Each backup includes:
- Full config file copy
- Timestamp
- Description
- Original path metadata

---

## 🔧 Building Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build
pyinstaller --onefile --windowed --name FieldTuner3 src/main.py

# Output: dist/FieldTuner3.exe
```

---

## 📜 Consolidated From

This project consolidates the best features from:

- **FieldTuner V2.0** - Modular architecture, bulletproof config manager
- **FieldTuner Max** - Search feature, CLI support, modern UI concepts
- **FieldTuner Reborn** - 326 settings parsing, comprehensive backup system
- **FieldTuner 1.0** - Keyboard shortcuts, preset system

---

## 🙏 Acknowledgments

- **Hans Yolo / Nobody621** - Original idea inspiration
- **SneakyTom** - Development and consolidation
- **PyQt6** - Excellent GUI framework
- **Cursor, Windsurf, Claude** - AI-assisted development

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

**Made with ❤️ by SneakyTom**

*Making Battlefield 6 configuration as smooth as butter*
