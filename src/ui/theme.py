"""
Theme - Modern dark theme for FieldTuner Ultimate.
Inspired by professional tools like WeMod and Discord.
"""

THEME = {
    'colors': {
        'bg_primary': '#1a1a2e',
        'bg_secondary': '#16213e',
        'bg_tertiary': '#0f3460',
        'bg_card': '#1f2940',
        'bg_hover': '#2a3f5f',
        
        'accent_primary': '#e94560',
        'accent_secondary': '#00d9ff',
        'accent_success': '#4ade80',
        'accent_warning': '#fbbf24',
        'accent_error': '#ef4444',
        
        'text_primary': '#ffffff',
        'text_secondary': '#a0aec0',
        'text_muted': '#718096',
        
        'border_primary': '#2d3748',
        'border_secondary': '#4a5568',
    },
    'fonts': {
        'family': 'Segoe UI',
        'size_xs': '10px',
        'size_sm': '12px',
        'size_md': '14px',
        'size_lg': '16px',
        'size_xl': '20px',
        'size_2xl': '24px',
    },
    'spacing': {
        'xs': '4px',
        'sm': '8px',
        'md': '12px',
        'lg': '16px',
        'xl': '24px',
        '2xl': '32px',
    },
    'radius': {
        'sm': '4px',
        'md': '8px',
        'lg': '12px',
        'xl': '16px',
        'full': '9999px',
    }
}


def get_stylesheet() -> str:
    """Generate the main application stylesheet."""
    c = THEME['colors']
    f = THEME['fonts']
    s = THEME['spacing']
    r = THEME['radius']
    
    return f"""
        /* Main Window */
        QMainWindow {{
            background-color: {c['bg_primary']};
        }}
        
        QWidget {{
            background-color: transparent;
            color: {c['text_primary']};
            font-family: {f['family']};
            font-size: {f['size_md']};
        }}
        
        /* Labels */
        QLabel {{
            color: {c['text_primary']};
            background: transparent;
        }}
        
        QLabel[class="title"] {{
            font-size: {f['size_2xl']};
            font-weight: bold;
        }}
        
        QLabel[class="subtitle"] {{
            font-size: {f['size_lg']};
            color: {c['text_secondary']};
        }}
        
        QLabel[class="muted"] {{
            color: {c['text_muted']};
            font-size: {f['size_sm']};
        }}
        
        /* Buttons */
        QPushButton {{
            background-color: {c['bg_tertiary']};
            color: {c['text_primary']};
            border: 1px solid {c['border_primary']};
            border-radius: {r['md']};
            padding: {s['sm']} {s['lg']};
            font-weight: 500;
            min-height: 32px;
        }}
        
        QPushButton:hover {{
            background-color: {c['bg_hover']};
            border-color: {c['accent_secondary']};
        }}
        
        QPushButton:pressed {{
            background-color: {c['bg_secondary']};
        }}
        
        QPushButton:disabled {{
            background-color: {c['bg_secondary']};
            color: {c['text_muted']};
            border-color: {c['border_primary']};
        }}
        
        QPushButton[class="primary"] {{
            background-color: {c['accent_primary']};
            border-color: {c['accent_primary']};
        }}
        
        QPushButton[class="primary"]:hover {{
            background-color: #d63d56;
        }}
        
        QPushButton[class="success"] {{
            background-color: {c['accent_success']};
            border-color: {c['accent_success']};
            color: #1a1a2e;
        }}
        
        QPushButton[class="success"]:hover {{
            background-color: #22c55e;
        }}
        
        /* Tab Widget */
        QTabWidget::pane {{
            background-color: {c['bg_secondary']};
            border: 1px solid {c['border_primary']};
            border-radius: {r['md']};
            padding: {s['md']};
        }}
        
        QTabBar::tab {{
            background-color: {c['bg_tertiary']};
            color: {c['text_secondary']};
            border: none;
            padding: {s['sm']} {s['xl']};
            margin-right: 2px;
            border-top-left-radius: {r['md']};
            border-top-right-radius: {r['md']};
        }}
        
        QTabBar::tab:selected {{
            background-color: {c['accent_primary']};
            color: {c['text_primary']};
        }}
        
        QTabBar::tab:hover:!selected {{
            background-color: {c['bg_hover']};
            color: {c['text_primary']};
        }}
        
        /* Scroll Area */
        QScrollArea {{
            background-color: transparent;
            border: none;
        }}
        
        QScrollBar:vertical {{
            background-color: {c['bg_secondary']};
            width: 10px;
            border-radius: 5px;
        }}
        
        QScrollBar::handle:vertical {{
            background-color: {c['border_secondary']};
            border-radius: 5px;
            min-height: 30px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background-color: {c['accent_secondary']};
        }}
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0;
        }}
        
        QScrollBar:horizontal {{
            background-color: {c['bg_secondary']};
            height: 10px;
            border-radius: 5px;
        }}
        
        QScrollBar::handle:horizontal {{
            background-color: {c['border_secondary']};
            border-radius: 5px;
            min-width: 30px;
        }}
        
        /* Line Edit */
        QLineEdit {{
            background-color: {c['bg_secondary']};
            color: {c['text_primary']};
            border: 1px solid {c['border_primary']};
            border-radius: {r['md']};
            padding: {s['sm']} {s['md']};
            selection-background-color: {c['accent_primary']};
        }}
        
        QLineEdit:focus {{
            border-color: {c['accent_secondary']};
        }}
        
        QLineEdit:disabled {{
            background-color: {c['bg_primary']};
            color: {c['text_muted']};
        }}
        
        /* Combo Box */
        QComboBox {{
            background-color: {c['bg_secondary']};
            color: {c['text_primary']};
            border: 1px solid {c['border_primary']};
            border-radius: {r['md']};
            padding: {s['sm']} {s['md']};
            min-height: 32px;
        }}
        
        QComboBox:hover {{
            border-color: {c['accent_secondary']};
        }}
        
        QComboBox::drop-down {{
            border: none;
            width: 24px;
        }}
        
        QComboBox::down-arrow {{
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 5px solid {c['text_secondary']};
        }}
        
        QComboBox QAbstractItemView {{
            background-color: {c['bg_secondary']};
            color: {c['text_primary']};
            border: 1px solid {c['border_primary']};
            selection-background-color: {c['accent_primary']};
        }}
        
        /* Slider */
        QSlider::groove:horizontal {{
            background-color: {c['bg_tertiary']};
            height: 6px;
            border-radius: 3px;
        }}
        
        QSlider::handle:horizontal {{
            background-color: {c['accent_primary']};
            width: 16px;
            height: 16px;
            margin: -5px 0;
            border-radius: 8px;
        }}
        
        QSlider::handle:horizontal:hover {{
            background-color: {c['accent_secondary']};
        }}
        
        QSlider::sub-page:horizontal {{
            background-color: {c['accent_primary']};
            border-radius: 3px;
        }}
        
        /* Spin Box */
        QSpinBox, QDoubleSpinBox {{
            background-color: {c['bg_secondary']};
            color: {c['text_primary']};
            border: 1px solid {c['border_primary']};
            border-radius: {r['md']};
            padding: {s['sm']};
        }}
        
        QSpinBox:focus, QDoubleSpinBox:focus {{
            border-color: {c['accent_secondary']};
        }}
        
        /* Check Box */
        QCheckBox {{
            color: {c['text_primary']};
            spacing: {s['sm']};
        }}
        
        QCheckBox::indicator {{
            width: 20px;
            height: 20px;
            border-radius: {r['sm']};
            border: 2px solid {c['border_secondary']};
            background-color: {c['bg_secondary']};
        }}
        
        QCheckBox::indicator:checked {{
            background-color: {c['accent_primary']};
            border-color: {c['accent_primary']};
        }}
        
        QCheckBox::indicator:hover {{
            border-color: {c['accent_secondary']};
        }}
        
        /* Group Box */
        QGroupBox {{
            background-color: {c['bg_card']};
            border: 1px solid {c['border_primary']};
            border-radius: {r['lg']};
            margin-top: 16px;
            padding: {s['lg']};
            font-weight: bold;
        }}
        
        QGroupBox::title {{
            subcontrol-origin: margin;
            left: {s['lg']};
            padding: 0 {s['sm']};
            color: {c['accent_secondary']};
        }}
        
        /* List Widget */
        QListWidget {{
            background-color: {c['bg_secondary']};
            border: 1px solid {c['border_primary']};
            border-radius: {r['md']};
            padding: {s['sm']};
        }}
        
        QListWidget::item {{
            padding: {s['sm']};
            border-radius: {r['sm']};
        }}
        
        QListWidget::item:selected {{
            background-color: {c['accent_primary']};
        }}
        
        QListWidget::item:hover:!selected {{
            background-color: {c['bg_hover']};
        }}
        
        /* Status Bar */
        QStatusBar {{
            background-color: {c['bg_secondary']};
            color: {c['text_secondary']};
            border-top: 1px solid {c['border_primary']};
        }}
        
        /* Message Box */
        QMessageBox {{
            background-color: {c['bg_primary']};
        }}
        
        QMessageBox QLabel {{
            color: {c['text_primary']};
        }}
        
        /* Tool Tip */
        QToolTip {{
            background-color: {c['bg_tertiary']};
            color: {c['text_primary']};
            border: 1px solid {c['border_primary']};
            border-radius: {r['sm']};
            padding: {s['sm']};
        }}
    """
