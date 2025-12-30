"""FieldTuner 3.0 - Stable UI"""
import sys
from pathlib import Path
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QComboBox, QStatusBar, QMessageBox, 
    QScrollArea, QFrame, QCheckBox, QDoubleSpinBox, QSpinBox,
    QStackedWidget, QListWidget, QListWidgetItem, QApplication,
    QSplitter, QTreeWidget, QTreeWidgetItem, QHeaderView
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor

# Direct config file access
CONFIG_PATH = Path.home() / "OneDrive" / "Documents" / "Battlefield 6" / "settings" / "steam" / "PROFSAVE_profile"
BACKUP_DIR = Path.home() / "AppData" / "Roaming" / "FieldTuner" / "backups"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FieldTuner 3.0")
        self.resize(1100, 750)
        self.settings = {}
        self.modified = set()
        self._setup_dark_palette()
        self._load_config()
        self._build_ui()
    
    def _setup_dark_palette(self):
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Base, QColor(45, 45, 45))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(55, 55, 55))
        palette.setColor(QPalette.ColorRole.Text, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Button, QColor(55, 55, 55))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        self.setPalette(palette)
        QApplication.instance().setPalette(palette)
    
    def _load_config(self):
        self.settings = {}
        self.config_path = None
        paths = [
            CONFIG_PATH,
            Path.home() / "Documents" / "Battlefield 6" / "settings" / "steam" / "PROFSAVE_profile",
            Path.home() / "Documents" / "Battlefield 6" / "settings" / "PROFSAVE_profile",
        ]
        for p in paths:
            if p.exists():
                self.config_path = p
                break
        if self.config_path:
            try:
                with open(self.config_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        line = line.strip()
                        if ' ' in line:
                            key, val = line.split(' ', 1)
                            self.settings[key] = val
            except Exception as e:
                print(f"Error loading config: {e}")
    
    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main = QHBoxLayout(central)
        main.setContentsMargins(0, 0, 0, 0)
        main.setSpacing(0)
        
        # Sidebar
        sidebar = QFrame()
        sidebar.setFixedWidth(180)
        sidebar.setStyleSheet("QFrame{background:#1a1a1a;border-right:1px solid #333}")
        sb_layout = QVBoxLayout(sidebar)
        sb_layout.setContentsMargins(10, 15, 10, 15)
        sb_layout.setSpacing(5)
        
        title = QLabel("FieldTuner 3.0")
        title.setStyleSheet("font-size:16px;font-weight:bold;color:#0af;padding:10px 0")
        sb_layout.addWidget(title)
        
        self.nav_btns = {}
        for name in ["Home", "Graphics", "Audio", "Input", "Backups"]:
            btn = QPushButton(name)
            btn.setCheckable(True)
            btn.setStyleSheet("""
                QPushButton{text-align:left;padding:10px;border:none;border-radius:5px;background:transparent;color:#aaa}
                QPushButton:hover{background:#2a2a2a;color:#fff}
                QPushButton:checked{background:#0af;color:#000;font-weight:bold}
            """)
            btn.clicked.connect(lambda c, n=name: self._nav(n))
            self.nav_btns[name] = btn
            sb_layout.addWidget(btn)
        
        sb_layout.addStretch()
        
        save_btn = QPushButton("Save Changes")
        save_btn.setStyleSheet("QPushButton{background:#0a5;color:#fff;padding:12px;border:none;border-radius:5px;font-weight:bold}QPushButton:hover{background:#0c7}")
        save_btn.clicked.connect(self._save)
        sb_layout.addWidget(save_btn)
        
        main.addWidget(sidebar)
        
        # Content
        content = QWidget()
        content.setStyleSheet("background:#222")
        cl = QVBoxLayout(content)
        cl.setContentsMargins(20, 20, 20, 20)
        
        self.pages = QStackedWidget()
        self.pages.addWidget(self._home_page())
        self.pages.addWidget(self._settings_page("GstRender"))
        self.pages.addWidget(self._settings_page("GstAudio"))
        self.pages.addWidget(self._settings_page("GstInput"))
        self.pages.addWidget(self._backups_page())
        
        cl.addWidget(self.pages)
        main.addWidget(content, 1)
        
        self.statusBar().showMessage(f"Loaded: {self.config_path.name if self.config_path else 'No config'} | {len(self.settings)} settings")
        self._nav("Home")
    
    def _nav(self, page):
        for n, b in self.nav_btns.items():
            b.setChecked(n == page)
        idx = {"Home": 0, "Graphics": 1, "Audio": 2, "Input": 3, "Backups": 4}.get(page, 0)
        self.pages.setCurrentIndex(idx)
    
    def _home_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(20)
        
        h = QLabel("Welcome to FieldTuner")
        h.setStyleSheet("font-size:24px;font-weight:bold;color:#fff")
        layout.addWidget(h)
        
        sub = QLabel("Battlefield 6 Configuration Tool")
        sub.setStyleSheet("color:#888;font-size:14px")
        layout.addWidget(sub)
        
        # Info cards
        info = QHBoxLayout()
        info.setSpacing(15)
        
        for title, val, color in [
            ("Config", self.config_path.name if self.config_path else "Not found", "#0af"),
            ("Settings", str(len(self.settings)), "#0a5"),
            ("Modified", str(len(self.modified)), "#fa0")
        ]:
            card = QFrame()
            card.setStyleSheet(f"QFrame{{background:#2a2a2a;border-radius:8px;border-left:3px solid {color}}}")
            card.setFixedSize(150, 70)
            cl = QVBoxLayout(card)
            cl.setContentsMargins(12, 10, 12, 10)
            t = QLabel(title)
            t.setStyleSheet("color:#888;font-size:11px")
            cl.addWidget(t)
            v = QLabel(val)
            v.setStyleSheet(f"color:{color};font-size:15px;font-weight:bold")
            cl.addWidget(v)
            info.addWidget(card)
        
        info.addStretch()
        layout.addLayout(info)
        
        # Quick actions
        qa = QLabel("Quick Actions")
        qa.setStyleSheet("font-size:16px;font-weight:bold;color:#fff;margin-top:20px")
        layout.addWidget(qa)
        
        btns = QHBoxLayout()
        btns.setSpacing(10)
        presets = [
            ("Esports", "#e44", {"GstRender.OverallGraphicsQuality": "0", "GstRender.VSyncMode": "0"}),
            ("Balanced", "#0a5", {"GstRender.OverallGraphicsQuality": "2"}),
            ("Quality", "#48f", {"GstRender.OverallGraphicsQuality": "3"}),
        ]
        for name, color, settings in presets:
            btn = QPushButton(name)
            btn.setStyleSheet(f"QPushButton{{background:{color};color:#fff;padding:12px 25px;border:none;border-radius:6px;font-weight:bold}}QPushButton:hover{{opacity:0.8}}")
            btn.clicked.connect(lambda c, s=settings, n=name: self._apply_preset(n, s))
            btns.addWidget(btn)
        btns.addStretch()
        layout.addLayout(btns)
        
        layout.addStretch()
        return page
    
    def _settings_page(self, prefix):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(10)
        
        # Header
        header = QHBoxLayout()
        title = QLabel(prefix.replace("Gst", ""))
        title.setStyleSheet("font-size:22px;font-weight:bold;color:#fff")
        header.addWidget(title)
        header.addStretch()
        
        search = QLineEdit()
        search.setPlaceholderText("Search...")
        search.setFixedWidth(200)
        search.setStyleSheet("QLineEdit{background:#333;border:1px solid #444;border-radius:5px;padding:8px;color:#fff}QLineEdit:focus{border-color:#0af}")
        header.addWidget(search)
        layout.addLayout(header)
        
        # Settings list
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea{border:none}")
        
        container = QWidget()
        container_layout = QVBoxLayout(container)
        container_layout.setSpacing(5)
        container_layout.setContentsMargins(0, 10, 0, 10)
        
        # Get settings for this prefix
        relevant = {k: v for k, v in self.settings.items() if k.startswith(prefix) and "ShaderBundle" not in k and "KeyBinding" not in k}
        
        for key, val in sorted(relevant.items()):
            row = self._create_setting_row(key, val)
            container_layout.addWidget(row)
        
        container_layout.addStretch()
        scroll.setWidget(container)
        layout.addWidget(scroll)
        
        # Connect search
        def filter_settings(text):
            text = text.lower()
            for i in range(container_layout.count() - 1):
                w = container_layout.itemAt(i).widget()
                if w:
                    w.setVisible(text in w.property("key").lower() if w.property("key") else True)
        search.textChanged.connect(filter_settings)
        
        return page
    
    def _create_setting_row(self, key, val):
        row = QFrame()
        row.setProperty("key", key)
        row.setStyleSheet("QFrame{background:#2a2a2a;border-radius:6px;padding:5px}QFrame:hover{background:#333}")
        layout = QHBoxLayout(row)
        layout.setContentsMargins(15, 10, 15, 10)
        
        # Name
        name = key.split('.')[-1]
        name_label = QLabel(name)
        name_label.setStyleSheet("font-weight:bold;color:#ddd")
        name_label.setFixedWidth(250)
        layout.addWidget(name_label)
        
        # Value control
        try:
            fval = float(val)
            is_bool = fval in (0.0, 1.0) and '.' not in val
            is_int = fval == int(fval) and '.' not in val
            
            if is_bool:
                ctrl = QCheckBox()
                ctrl.setChecked(int(fval) == 1)
                ctrl.setStyleSheet("QCheckBox::indicator{width:20px;height:20px}QCheckBox::indicator:unchecked{background:#444;border:2px solid #555;border-radius:4px}QCheckBox::indicator:checked{background:#0af;border:2px solid #0af;border-radius:4px}")
                ctrl.stateChanged.connect(lambda s, k=key: self._change(k, "1" if s else "0"))
            elif is_int:
                ctrl = QSpinBox()
                ctrl.setRange(-999999, 999999)
                ctrl.setValue(int(fval))
                ctrl.setStyleSheet("QSpinBox{background:#333;border:1px solid #444;border-radius:4px;padding:5px;color:#fff;min-width:100px}")
                ctrl.valueChanged.connect(lambda v, k=key: self._change(k, str(v)))
            else:
                ctrl = QDoubleSpinBox()
                ctrl.setRange(-999999, 999999)
                ctrl.setDecimals(6)
                ctrl.setValue(fval)
                ctrl.setStyleSheet("QDoubleSpinBox{background:#333;border:1px solid #444;border-radius:4px;padding:5px;color:#fff;min-width:100px}")
                ctrl.valueChanged.connect(lambda v, k=key: self._change(k, f"{v:.6f}"))
        except:
            ctrl = QLineEdit(val)
            ctrl.setStyleSheet("QLineEdit{background:#333;border:1px solid #444;border-radius:4px;padding:5px;color:#fff;min-width:150px}")
            ctrl.textChanged.connect(lambda t, k=key: self._change(k, t))
        
        layout.addWidget(ctrl)
        layout.addStretch()
        return row
    
    def _backups_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        h = QLabel("Backups")
        h.setStyleSheet("font-size:22px;font-weight:bold;color:#fff")
        layout.addWidget(h)
        
        # Buttons
        btns = QHBoxLayout()
        create = QPushButton("Create Backup")
        create.setStyleSheet("QPushButton{background:#0af;color:#000;padding:10px 20px;border:none;border-radius:5px;font-weight:bold}")
        create.clicked.connect(self._create_backup)
        btns.addWidget(create)
        btns.addStretch()
        layout.addLayout(btns)
        
        # List
        self.backup_list = QListWidget()
        self.backup_list.setStyleSheet("QListWidget{background:#2a2a2a;border:1px solid #333;border-radius:6px}QListWidget::item{padding:10px;border-bottom:1px solid #333}QListWidget::item:selected{background:#0af;color:#000}")
        self._refresh_backups()
        layout.addWidget(self.backup_list)
        
        # Actions
        acts = QHBoxLayout()
        restore = QPushButton("Restore")
        restore.clicked.connect(self._restore_backup)
        acts.addWidget(restore)
        delete = QPushButton("Delete")
        delete.clicked.connect(self._delete_backup)
        acts.addWidget(delete)
        acts.addStretch()
        layout.addLayout(acts)
        
        return page
    
    def _change(self, key, val):
        self.settings[key] = val
        self.modified.add(key)
        self.statusBar().showMessage(f"{len(self.modified)} unsaved changes")
    
    def _apply_preset(self, name, settings):
        if QMessageBox.question(self, "Apply Preset", f"Apply {name} preset?") == QMessageBox.StandardButton.Yes:
            for k, v in settings.items():
                self.settings[k] = v
                self.modified.add(k)
            self.statusBar().showMessage(f"Applied {name} preset - {len(self.modified)} changes pending")
    
    def _save(self):
        if not self.config_path:
            QMessageBox.warning(self, "Error", "No config file found")
            return
        try:
            # Backup first
            self._create_backup()
            # Write
            lines = []
            for k, v in sorted(self.settings.items()):
                lines.append(f"{k} {v}")
            with open(self.config_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines) + '\n')
            self.modified.clear()
            self.statusBar().showMessage("Saved successfully!")
            QMessageBox.information(self, "Saved", "Configuration saved!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Save failed: {e}")
    
    def _create_backup(self):
        if not self.config_path:
            return
        try:
            BACKUP_DIR.mkdir(parents=True, exist_ok=True)
            from datetime import datetime
            name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            import shutil
            shutil.copy(self.config_path, BACKUP_DIR / name)
            self._refresh_backups()
        except Exception as e:
            print(f"Backup error: {e}")
    
    def _refresh_backups(self):
        if hasattr(self, 'backup_list'):
            self.backup_list.clear()
            if BACKUP_DIR.exists():
                for f in sorted(BACKUP_DIR.glob("*.txt"), reverse=True):
                    self.backup_list.addItem(f.name)
    
    def _restore_backup(self):
        item = self.backup_list.currentItem()
        if not item:
            return
        if QMessageBox.question(self, "Restore", f"Restore {item.text()}?") == QMessageBox.StandardButton.Yes:
            try:
                import shutil
                shutil.copy(BACKUP_DIR / item.text(), self.config_path)
                self._load_config()
                self.statusBar().showMessage("Restored!")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
    
    def _delete_backup(self):
        item = self.backup_list.currentItem()
        if item and QMessageBox.question(self, "Delete", f"Delete {item.text()}?") == QMessageBox.StandardButton.Yes:
            try:
                (BACKUP_DIR / item.text()).unlink()
                self._refresh_backups()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
