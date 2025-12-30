"""
MainWindow - Modern, simplified main window for FieldTuner Ultimate.
Features a clean tabbed interface with search, presets, and settings management.
"""

import sys
from pathlib import Path
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget,
    QLabel, QLineEdit, QPushButton, QComboBox, QStatusBar,
    QMessageBox, QScrollArea, QGridLayout, QGroupBox, QSlider,
    QCheckBox, QDoubleSpinBox, QSpinBox, QFrame, QSplitter,
    QListWidget, QListWidgetItem, QStackedWidget, QSizePolicy
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QIcon

from ui.theme import get_stylesheet, THEME
from core import (
    ConfigManager, BackupManager, SETTINGS_DATABASE,
    get_setting_info, search_settings,
    PRESETS, apply_preset
)
from core.settings_database import get_categories, get_settings_by_category


class MainWindow(QMainWindow):
    """Main application window with modern UI."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FieldTuner 3.0 - Battlefield 6 Configuration Tool")
        self.setMinimumSize(1100, 750)
        self.resize(1200, 800)
        
        # Apply theme
        self.setStyleSheet(get_stylesheet())
        
        # Initialize managers
        self.config_manager = ConfigManager()
        self.backup_manager = BackupManager()
        
        # Track modified settings
        self.modified_settings = set()
        
        # Setup UI
        self._setup_ui()
        self._update_status()
        
        # Create initial backup if config loaded
        if self.config_manager.config_path:
            self.backup_manager.create_backup(
                self.config_manager.config_path, 
                "app_start"
            )
    
    def _setup_ui(self):
        """Setup the main UI layout."""
        central = QWidget()
        self.setCentralWidget(central)
        
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Header
        self._create_header(layout)
        
        # Main content area
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(16, 16, 16, 16)
        
        # Tab widget
        self.tabs = QTabWidget()
        self._create_tabs()
        content_layout.addWidget(self.tabs)
        
        layout.addWidget(content)
        
        # Status bar
        self._create_status_bar()
    
    def _create_header(self, parent_layout):
        """Create the application header."""
        header = QWidget()
        header.setFixedHeight(70)
        header.setStyleSheet(f"""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {THEME['colors']['accent_primary']}, 
                stop:1 #c13b51);
            border-bottom: 2px solid {THEME['colors']['border_primary']};
        """)
        
        layout = QHBoxLayout(header)
        layout.setContentsMargins(24, 12, 24, 12)
        
        # Logo/Title
        title = QLabel("🎮 FieldTuner 3.0")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
        """)
        layout.addWidget(title)
        
        # Search box
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("🔍 Search settings (e.g., 'vsync', 'fps', 'motion blur')")
        self.search_box.setFixedWidth(350)
        self.search_box.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255,255,255,0.15);
                border: 1px solid rgba(255,255,255,0.3);
                border-radius: 8px;
                padding: 8px 12px;
                color: white;
            }
            QLineEdit:focus {
                background-color: rgba(255,255,255,0.2);
                border-color: white;
            }
        """)
        self.search_box.textChanged.connect(self._on_search)
        layout.addWidget(self.search_box)
        
        layout.addStretch()
        
        # Save button
        save_btn = QPushButton("💾 Save Changes")
        save_btn.setProperty("class", "success")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #4ade80;
                color: #1a1a2e;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #22c55e;
            }
        """)
        save_btn.clicked.connect(self._save_config)
        layout.addWidget(save_btn)
        
        parent_layout.addWidget(header)
    
    def _create_tabs(self):
        """Create all application tabs."""
        # Dashboard tab
        self.tabs.addTab(self._create_dashboard_tab(), "🏠 Dashboard")
        
        # Settings tabs by category
        self.tabs.addTab(self._create_category_tab("Graphics"), "🖥️ Graphics")
        self.tabs.addTab(self._create_category_tab("Performance"), "⚡ Performance")
        self.tabs.addTab(self._create_category_tab("Audio"), "🔊 Audio")
        self.tabs.addTab(self._create_category_tab("Input"), "🎮 Input")
        
        # Presets tab
        self.tabs.addTab(self._create_presets_tab(), "✨ Presets")
        
        # Backup tab
        self.tabs.addTab(self._create_backup_tab(), "💾 Backups")
        
        # Search results tab (hidden initially)
        self.search_results_tab = self._create_search_results_tab()
        self.search_tab_index = self.tabs.addTab(self.search_results_tab, "🔍 Search Results")
        self.tabs.setTabVisible(self.search_tab_index, False)
    
    def _create_dashboard_tab(self) -> QWidget:
        """Create the dashboard/overview tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(20)
        
        # Welcome section
        welcome = QLabel("Welcome to FieldTuner Ultimate")
        welcome.setStyleSheet("font-size: 28px; font-weight: bold; color: white;")
        layout.addWidget(welcome)
        
        subtitle = QLabel("The ultimate Battlefield 6 configuration tool")
        subtitle.setStyleSheet(f"font-size: 16px; color: {THEME['colors']['text_secondary']};")
        layout.addWidget(subtitle)
        
        layout.addSpacing(20)
        
        # Status cards
        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(16)
        
        # Config status card
        config_card = self._create_status_card(
            "📁 Config File",
            self.config_manager.config_path.name if self.config_manager.config_path else "Not loaded",
            THEME['colors']['accent_secondary']
        )
        cards_layout.addWidget(config_card)
        
        # Settings count card
        settings_card = self._create_status_card(
            "⚙️ Settings Loaded",
            str(self.config_manager.get_setting_count()),
            THEME['colors']['accent_success']
        )
        cards_layout.addWidget(settings_card)
        
        # Backups card
        backups_card = self._create_status_card(
            "💾 Backups",
            str(self.backup_manager.get_backup_count()),
            THEME['colors']['accent_warning']
        )
        cards_layout.addWidget(backups_card)
        
        cards_layout.addStretch()
        layout.addLayout(cards_layout)
        
        layout.addSpacing(30)
        
        # Quick actions
        actions_label = QLabel("Quick Actions")
        actions_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(actions_label)
        
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(12)
        
        for preset_key, preset in list(PRESETS.items())[:4]:
            btn = QPushButton(f"{preset['icon']} {preset['name']}")
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {preset['color']};
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 15px 25px;
                    font-weight: bold;
                    font-size: 14px;
                }}
                QPushButton:hover {{
                    opacity: 0.9;
                }}
            """)
            btn.setToolTip(preset['description'])
            btn.clicked.connect(lambda checked, k=preset_key: self._apply_preset(k))
            actions_layout.addWidget(btn)
        
        actions_layout.addStretch()
        layout.addLayout(actions_layout)
        
        layout.addStretch()
        
        # Footer note
        footer = QLabel("Made with ❤️ by SneakyTom • Consolidated from multiple FieldTuner versions")
        footer.setStyleSheet(f"color: {THEME['colors']['text_muted']}; font-size: 12px;")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(footer)
        
        return widget
    
    def _create_status_card(self, title: str, value: str, color: str) -> QFrame:
        """Create a status card widget."""
        card = QFrame()
        card.setFixedSize(200, 100)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: {THEME['colors']['bg_card']};
                border: 1px solid {THEME['colors']['border_primary']};
                border-radius: 12px;
                border-left: 4px solid {color};
            }}
        """)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(16, 12, 16, 12)
        
        title_label = QLabel(title)
        title_label.setStyleSheet(f"color: {THEME['colors']['text_secondary']}; font-size: 12px;")
        layout.addWidget(title_label)
        
        value_label = QLabel(value)
        value_label.setStyleSheet(f"color: {color}; font-size: 20px; font-weight: bold;")
        layout.addWidget(value_label)
        
        return card
    
    def _create_category_tab(self, category: str) -> QWidget:
        """Create a settings tab for a specific category."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Scroll area for settings
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setSpacing(12)
        
        # Get settings for this category
        settings = get_settings_by_category(category)
        
        # Group by subcategory
        subcategories = {}
        for key, info in settings.items():
            subcat = info.get('subcategory', 'General')
            if subcat not in subcategories:
                subcategories[subcat] = {}
            subcategories[subcat][key] = info
        
        # Create groups
        for subcat_name, subcat_settings in subcategories.items():
            group = QGroupBox(subcat_name)
            group_layout = QGridLayout(group)
            group_layout.setSpacing(12)
            
            row = 0
            for key, info in subcat_settings.items():
                # Label
                label = QLabel(info['name'])
                label.setToolTip(info.get('tooltip', ''))
                group_layout.addWidget(label, row, 0)
                
                # Control widget
                control = self._create_setting_control(key, info)
                group_layout.addWidget(control, row, 1)
                
                row += 1
            
            scroll_layout.addWidget(group)
        
        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)
        
        return widget
    
    def _create_setting_control(self, key: str, info: dict) -> QWidget:
        """Create the appropriate control widget for a setting."""
        setting_type = info.get('type', 'float')
        current_value = self.config_manager.get(key)
        
        if setting_type == 'bool':
            control = QCheckBox()
            if current_value is not None:
                control.setChecked(str(current_value) == '1')
            control.stateChanged.connect(lambda state, k=key: self._on_setting_changed(k, '1' if state else '0'))
            
        elif 'options' in info:
            control = QComboBox()
            control.setMinimumWidth(150)
            for val, text in info['options'].items():
                control.addItem(text, val)
            if current_value is not None:
                try:
                    index = list(info['options'].keys()).index(int(float(current_value)))
                    control.setCurrentIndex(index)
                except (ValueError, IndexError):
                    pass
            control.currentIndexChanged.connect(lambda idx, k=key, c=control: self._on_setting_changed(k, str(c.currentData())))
            
        elif setting_type == 'int':
            control = QSpinBox()
            control.setMinimum(int(info.get('range', [0, 100])[0]))
            control.setMaximum(int(info.get('range', [0, 100])[1]))
            if current_value is not None:
                try:
                    control.setValue(int(float(current_value)))
                except ValueError:
                    pass
            control.valueChanged.connect(lambda val, k=key: self._on_setting_changed(k, str(val)))
            
        else:  # float
            control = QDoubleSpinBox()
            control.setMinimum(float(info.get('range', [0, 1])[0]))
            control.setMaximum(float(info.get('range', [0, 1])[1]))
            control.setDecimals(2)
            control.setSingleStep(0.1)
            if current_value is not None:
                try:
                    control.setValue(float(current_value))
                except ValueError:
                    pass
            control.valueChanged.connect(lambda val, k=key: self._on_setting_changed(k, f"{val:.6f}"))
        
        control.setToolTip(info.get('tooltip', ''))
        return control
    
    def _create_presets_tab(self) -> QWidget:
        """Create the presets tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(20)
        
        title = QLabel("Performance Presets")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)
        
        desc = QLabel("Apply optimized settings for different playstyles")
        desc.setStyleSheet(f"color: {THEME['colors']['text_secondary']};")
        layout.addWidget(desc)
        
        layout.addSpacing(20)
        
        # Preset cards
        presets_layout = QGridLayout()
        presets_layout.setSpacing(16)
        
        col = 0
        row = 0
        for preset_key, preset in PRESETS.items():
            card = self._create_preset_card(preset_key, preset)
            presets_layout.addWidget(card, row, col)
            col += 1
            if col >= 3:
                col = 0
                row += 1
        
        layout.addLayout(presets_layout)
        layout.addStretch()
        
        return widget
    
    def _create_preset_card(self, preset_key: str, preset: dict) -> QFrame:
        """Create a preset card."""
        card = QFrame()
        card.setFixedSize(280, 180)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: {THEME['colors']['bg_card']};
                border: 2px solid {THEME['colors']['border_primary']};
                border-radius: 12px;
            }}
            QFrame:hover {{
                border-color: {preset['color']};
            }}
        """)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(16, 16, 16, 16)
        
        # Header
        header = QLabel(f"{preset['icon']} {preset['name']}")
        header.setStyleSheet(f"font-size: 18px; font-weight: bold; color: {preset['color']};")
        layout.addWidget(header)
        
        # Description
        desc = QLabel(preset['description'])
        desc.setWordWrap(True)
        desc.setStyleSheet(f"color: {THEME['colors']['text_secondary']}; font-size: 12px;")
        layout.addWidget(desc)
        
        layout.addStretch()
        
        # Apply button
        btn = QPushButton("Apply Preset")
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {preset['color']};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                opacity: 0.9;
            }}
        """)
        btn.clicked.connect(lambda: self._apply_preset(preset_key))
        layout.addWidget(btn)
        
        return card
    
    def _create_backup_tab(self) -> QWidget:
        """Create the backup management tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(16)
        
        # Header
        header_layout = QHBoxLayout()
        title = QLabel("Backup Manager")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        create_btn = QPushButton("➕ Create Backup")
        create_btn.clicked.connect(self._create_backup)
        header_layout.addWidget(create_btn)
        
        layout.addLayout(header_layout)
        
        # Backup list
        self.backup_list = QListWidget()
        self.backup_list.setMinimumHeight(300)
        self._refresh_backup_list()
        layout.addWidget(self.backup_list)
        
        # Actions
        actions_layout = QHBoxLayout()
        
        restore_btn = QPushButton("♻️ Restore Selected")
        restore_btn.clicked.connect(self._restore_backup)
        actions_layout.addWidget(restore_btn)
        
        delete_btn = QPushButton("🗑️ Delete Selected")
        delete_btn.clicked.connect(self._delete_backup)
        actions_layout.addWidget(delete_btn)
        
        actions_layout.addStretch()
        
        refresh_btn = QPushButton("🔄 Refresh")
        refresh_btn.clicked.connect(self._refresh_backup_list)
        actions_layout.addWidget(refresh_btn)
        
        layout.addLayout(actions_layout)
        
        return widget
    
    def _create_search_results_tab(self) -> QWidget:
        """Create the search results tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        self.search_results_label = QLabel("Search results will appear here")
        self.search_results_label.setStyleSheet(f"color: {THEME['colors']['text_secondary']};")
        layout.addWidget(self.search_results_label)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        self.search_results_content = QWidget()
        self.search_results_layout = QVBoxLayout(self.search_results_content)
        scroll.setWidget(self.search_results_content)
        
        layout.addWidget(scroll)
        
        return widget
    
    def _create_status_bar(self):
        """Create the status bar."""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self._update_status()
    
    def _update_status(self):
        """Update the status bar."""
        if self.config_manager.config_path:
            status = f"📁 {self.config_manager.config_path.name} | ⚙️ {self.config_manager.get_setting_count()} settings"
            if self.modified_settings:
                status += f" | ✏️ {len(self.modified_settings)} modified"
        else:
            status = "⚠️ No config file loaded - Please ensure BF6 has been run at least once"
        
        self.status_bar.showMessage(status)
    
    def _on_search(self, text: str):
        """Handle search input."""
        if not text.strip():
            self.tabs.setTabVisible(self.search_tab_index, False)
            return
        
        # Show search tab
        self.tabs.setTabVisible(self.search_tab_index, True)
        self.tabs.setCurrentIndex(self.search_tab_index)
        
        # Clear previous results
        while self.search_results_layout.count():
            item = self.search_results_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Search
        results = search_settings(text)
        
        self.search_results_label.setText(f"Found {len(results)} settings matching '{text}'")
        
        for key, info in results.items():
            group = QGroupBox(f"{info['name']} ({info.get('category', 'Other')})")
            group_layout = QHBoxLayout(group)
            
            control = self._create_setting_control(key, info)
            group_layout.addWidget(QLabel(key))
            group_layout.addStretch()
            group_layout.addWidget(control)
            
            self.search_results_layout.addWidget(group)
        
        self.search_results_layout.addStretch()
    
    def _on_setting_changed(self, key: str, value: str):
        """Handle setting value change."""
        self.config_manager.set(key, value)
        self.modified_settings.add(key)
        self._update_status()
    
    def _apply_preset(self, preset_key: str):
        """Apply a preset."""
        if self.config_manager.is_battlefield_running():
            QMessageBox.warning(self, "Game Running", 
                "Please close Battlefield 6 before applying presets.")
            return
        
        reply = QMessageBox.question(
            self, "Apply Preset",
            f"Apply '{PRESETS[preset_key]['name']}' preset?\n\nThis will modify {len(PRESETS[preset_key]['settings'])} settings.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            success, message = apply_preset(self.config_manager, preset_key)
            if success:
                self.modified_settings.update(PRESETS[preset_key]['settings'].keys())
                self._update_status()
                QMessageBox.information(self, "Success", message)
            else:
                QMessageBox.warning(self, "Error", message)
    
    def _save_config(self):
        """Save configuration changes."""
        if not self.config_manager.config_path:
            QMessageBox.warning(self, "No Config", "No configuration file loaded.")
            return
        
        if self.config_manager.is_battlefield_running():
            QMessageBox.warning(self, "Game Running",
                "Please close Battlefield 6 before saving changes.")
            return
        
        # Create backup first
        self.backup_manager.create_backup(self.config_manager.config_path, "before_save")
        
        success, message = self.config_manager.save()
        
        if success:
            self.modified_settings.clear()
            self._update_status()
            QMessageBox.information(self, "Saved", f"✅ {message}")
        else:
            QMessageBox.warning(self, "Save Failed", message)
    
    def _create_backup(self):
        """Create a manual backup."""
        if not self.config_manager.config_path:
            QMessageBox.warning(self, "No Config", "No configuration file to backup.")
            return
        
        path = self.backup_manager.create_backup(self.config_manager.config_path, "manual")
        if path:
            self._refresh_backup_list()
            QMessageBox.information(self, "Backup Created", f"Backup saved to:\n{path.name}")
        else:
            QMessageBox.warning(self, "Backup Failed", "Failed to create backup.")
    
    def _restore_backup(self):
        """Restore selected backup."""
        item = self.backup_list.currentItem()
        if not item:
            QMessageBox.warning(self, "No Selection", "Please select a backup to restore.")
            return
        
        backup_name = item.data(Qt.ItemDataRole.UserRole)
        
        reply = QMessageBox.question(
            self, "Restore Backup",
            f"Restore backup '{backup_name}'?\n\nThis will overwrite your current settings.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            success, message = self.backup_manager.restore_backup(
                backup_name, self.config_manager.config_path
            )
            if success:
                self.config_manager.reload()
                self.modified_settings.clear()
                self._update_status()
                QMessageBox.information(self, "Restored", message)
            else:
                QMessageBox.warning(self, "Restore Failed", message)
    
    def _delete_backup(self):
        """Delete selected backup."""
        item = self.backup_list.currentItem()
        if not item:
            QMessageBox.warning(self, "No Selection", "Please select a backup to delete.")
            return
        
        backup_name = item.data(Qt.ItemDataRole.UserRole)
        
        reply = QMessageBox.question(
            self, "Delete Backup",
            f"Delete backup '{backup_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            success, message = self.backup_manager.delete_backup(backup_name)
            if success:
                self._refresh_backup_list()
            else:
                QMessageBox.warning(self, "Delete Failed", message)
    
    def _refresh_backup_list(self):
        """Refresh the backup list."""
        self.backup_list.clear()
        
        for backup in self.backup_manager.get_backups():
            metadata = backup['metadata']
            text = f"📦 {backup['name']}"
            if 'description' in metadata and metadata['description']:
                text += f" - {metadata['description']}"
            
            item = QListWidgetItem(text)
            item.setData(Qt.ItemDataRole.UserRole, backup['name'])
            self.backup_list.addItem(item)
