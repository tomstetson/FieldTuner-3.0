"""
FieldTuner 3.0 - Main Entry Point
Battlefield 6 Configuration Tool
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from ui.main_window import MainWindow


def main():
    """Main application entry point."""
    try:
        # Create application
        app = QApplication(sys.argv)
        app.setApplicationName("FieldTuner 3.0")
        app.setApplicationVersion("1.0.0")
        app.setOrganizationName("SneakyTom")
        
        # Set default font
        font = QFont("Segoe UI", 10)
        app.setFont(font)
        
        # Create and show main window
        window = MainWindow()
        window.show()
        
        # Show welcome message if config loaded
        if window.config_manager.config_path:
            QMessageBox.information(
                window,
                "🎮 FieldTuner 3.0",
                f"✅ Configuration loaded successfully!\n\n"
                f"📁 File: {window.config_manager.config_path.name}\n"
                f"⚙️ Settings: {window.config_manager.get_setting_count()}\n"
                f"💾 Auto-backup created\n\n"
                f"Ready to optimize your Battlefield 6 experience!"
            )
        else:
            QMessageBox.warning(
                window,
                "⚠️ Config Not Found",
                "Could not find Battlefield 6 configuration file.\n\n"
                "Please ensure:\n"
                "• Battlefield 6 is installed\n"
                "• You have run the game at least once\n"
                "• Config file exists in Documents/Battlefield 6/settings/\n\n"
                "You can also use a backup config from a text-format backup folder."
            )
        
        # Run application
        return app.exec()
        
    except Exception as e:
        QMessageBox.critical(
            None,
            "Critical Error",
            f"FieldTuner 3.0 encountered an error:\n\n{str(e)}"
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
