from PyQt6.QtWidgets import (
    QMainWindow, QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizeGrip
)
from PyQt6.QtGui import QKeySequence, QShortcut, QFontDatabase, QTextCursor
from PyQt6.QtCore import Qt, QTimer

from .command_palette import CommandPalette
from .title_bar import CustomTitleBar
from .actions.registry import get_all_actions


READY_MESSAGE = "Ready  ·  Press Ctrl+K to open the command palette"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Frameless – we draw our own title bar.
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("uboop")
        self.resize(1000, 700)
        self.setMinimumSize(480, 320)

        # ---- central layout ------------------------------------------------
        central_widget = QWidget()
        central_widget.setObjectName("centralWidget")
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Custom title bar
        self.title_bar = CustomTitleBar(self)
        main_layout.addWidget(self.title_bar)

        # Editor
        self.editor = QTextEdit()
        self.editor.setObjectName("editor")
        self.editor.setAcceptRichText(False)
        self.editor.setPlaceholderText(
            "Paste or type your text here, then press Ctrl+K to run an action…"
        )
        mono = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        mono.setPointSize(11)
        self.editor.setFont(mono)
        main_layout.addWidget(self.editor, 1)

        # Status bar (custom, fits the dark theme & holds a size grip)
        self.status_bar = QWidget()
        self.status_bar.setObjectName("statusBar")
        self.status_bar.setFixedHeight(26)
        status_layout = QHBoxLayout(self.status_bar)
        status_layout.setContentsMargins(10, 0, 4, 0)
        status_layout.setSpacing(12)

        self.status_message = QLabel(READY_MESSAGE)
        self.status_message.setObjectName("statusMessage")
        status_layout.addWidget(self.status_message, 1)

        self.counts_label = QLabel()
        self.counts_label.setObjectName("statusCounts")
        status_layout.addWidget(self.counts_label)

        self.size_grip = QSizeGrip(self.status_bar)
        status_layout.addWidget(
            self.size_grip, 0,
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight,
        )

        main_layout.addWidget(self.status_bar)

        # ---- styling -------------------------------------------------------
        self.setStyleSheet(
            """
            QWidget#centralWidget {
                background-color: #1e1e1e;
            }
            QTextEdit#editor {
                background-color: #1e1e1e;
                color: #e8e8e8;
                border: none;
                padding: 12px 14px;
                selection-background-color: #094771;
            }
            QWidget#statusBar {
                background-color: #252526;
                border-top: 1px solid #1a1a1a;
            }
            QLabel#statusMessage, QLabel#statusCounts {
                color: #b8b8b8;
                font-size: 11px;
            }
            """
        )

        # ---- actions & shortcuts ------------------------------------------
        self.actions_map = get_all_actions()

        self._add_shortcut("Ctrl+K", self.open_palette)
        self._add_shortcut("Ctrl+Shift+P", self.open_palette)
        self._add_shortcut("Ctrl+Q", self.close)

        # Live counts
        self.editor.textChanged.connect(self._update_counts)
        self._update_counts()

        # Auto-clear transient status messages
        self._status_timer = QTimer(self)
        self._status_timer.setSingleShot(True)
        self._status_timer.timeout.connect(
            lambda: self.status_message.setText(READY_MESSAGE)
        )

    # ----- helpers ----------------------------------------------------------

    def _add_shortcut(self, sequence: str, slot):
        sc = QShortcut(QKeySequence(sequence), self)
        sc.activated.connect(slot)
        return sc

    def _update_counts(self):
        text = self.editor.toPlainText()
        chars = len(text)
        lines = text.count("\n") + 1 if text else 0
        self.counts_label.setText(f"{lines} lines · {chars} chars")

    def _flash_status(self, message: str, ms: int = 4000):
        self.status_message.setText(message)
        self._status_timer.start(ms)

    # ----- palette ----------------------------------------------------------

    def open_palette(self):
        palette = CommandPalette(self.actions_map, self)
        palette.action_selected.connect(self.execute_action)

        palette.adjustSize()
        win_geo = self.geometry()
        x = win_geo.x() + (win_geo.width() - palette.width()) // 2
        y = win_geo.y() + max(60, win_geo.height() // 6)
        palette.move(x, y)

        palette.exec()

    # ----- run an action ----------------------------------------------------

    def execute_action(self, action_name):
        action = self.actions_map.get(action_name)
        if action is None:
            self._flash_status(f"Unknown action: {action_name}")
            return

        text = self.editor.toPlainText()
        try:
            result = action.run(text)
        except Exception as exc:  # noqa: BLE001 – surface any failure
            self._flash_status(f"✖ {action_name} failed: {exc}", ms=6000)
            return

        if result is None:
            self._flash_status(f"✔ {action_name} (no output)")
            return

        # Replace editor contents while preserving the undo stack so Ctrl+Z
        # restores the pre-action text.
        cursor = self.editor.textCursor()
        cursor.beginEditBlock()
        cursor.select(QTextCursor.SelectionType.Document)
        cursor.removeSelectedText()
        cursor.insertText(str(result))
        cursor.endEditBlock()

        self._flash_status(f"✔ {action_name} applied")
