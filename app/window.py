from PyQt6.QtWidgets import QMainWindow, QTextEdit
from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtCore import Qt

from .command_palette import CommandPalette
from .actions.registry import get_all_actions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Utility App")
        self.resize(1000, 700)

        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        self.actions = get_all_actions()

        self.shortcut = QShortcut(QKeySequence("Ctrl+K"), self)
        self.shortcut.activated.connect(self.open_palette)

    def open_palette(self):
        palette = CommandPalette(self.actions, self)
        palette.action_selected.connect(self.execute_action)

        # center palette
        palette.move(
            self.geometry().center() - palette.rect().center()
        )

        palette.exec()

    def execute_action(self, action_name):
        action = self.actions[action_name]
        text = self.editor.toPlainText()

        result = action.run(text)

        if result is not None:
            self.editor.setPlainText(result)
