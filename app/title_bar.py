from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QMouseEvent


class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.dragging = False
        self.drag_position = QPoint()

        # Enable mouse tracking for the title bar
        self.setMouseTracking(True)

        self.setFixedHeight(40)
        self.setStyleSheet("""
            CustomTitleBar {
                background-color: #2d2d2d;
                border-bottom: 1px solid #1a1a1a;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
                padding-left: 10px;
            }
            QPushButton {
                background-color: transparent;
                border: none;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                padding: 0px 15px;
                min-width: 40px;
                max-width: 40px;
            }
            QPushButton:hover {
                background-color: #404040;
            }
            QPushButton#closeButton:hover {
                background-color: #e81123;
            }
        """)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Title label
        self.title_label = QLabel("uboop")
        self.title_label.setMouseTracking(True)
        # Let drag/double-click events fall through to the title bar.
        self.title_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        layout.addWidget(self.title_label)

        # Spacer
        layout.addStretch()

        # Window control buttons
        self.minimize_button = QPushButton("−")
        self.minimize_button.setToolTip("Minimize")
        self.minimize_button.clicked.connect(self.minimize_window)
        layout.addWidget(self.minimize_button)

        self.maximize_button = QPushButton("□")
        self.maximize_button.setToolTip("Maximize")
        self.maximize_button.clicked.connect(self.toggle_maximize)
        layout.addWidget(self.maximize_button)

        self.close_button = QPushButton("×")
        self.close_button.setObjectName("closeButton")
        self.close_button.setToolTip("Close")
        self.close_button.clicked.connect(self.close_window)
        layout.addWidget(self.close_button)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() != Qt.MouseButton.LeftButton:
            return super().mousePressEvent(event)

        # Prefer the compositor-driven system move — this is the only
        # reliable way to drag a frameless window on Wayland and on most
        # X11 window managers. Falls back to manual move() if it fails.
        win = self.window().windowHandle() if self.window() else None
        if win is not None and win.startSystemMove():
            self.dragging = False
            event.accept()
            return

        self.dragging = True
        self.drag_position = event.globalPosition().toPoint() - self.parent_window.pos()
        event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging and event.buttons() & Qt.MouseButton.LeftButton:
            self.parent_window.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = False
        event.accept()

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.toggle_maximize()
            event.accept()

    def minimize_window(self):
        if self.parent_window:
            self.parent_window.showMinimized()

    def toggle_maximize(self):
        if self.parent_window:
            if self.parent_window.isMaximized():
                self.parent_window.showNormal()
                self.maximize_button.setText("□")
            else:
                self.parent_window.showMaximized()
                self.maximize_button.setText("❐")

    def close_window(self):
        if self.parent_window:
            self.parent_window.close()

    def set_title(self, title: str):
        self.title_label.setText(title)

