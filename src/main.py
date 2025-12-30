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
        app = QApplication(sys.argv)
        app.setApplicationName("FieldTuner 3.0")
        app.setApplicationVersion("1.0.0")
        app.setOrganizationName("SneakyTom")
        
        font = QFont("Segoe UI", 10)
        app.setFont(font)
        
        window = MainWindow()
        window.show()
        
        return app.exec()
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
