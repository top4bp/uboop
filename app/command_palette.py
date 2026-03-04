from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem
from PyQt6.QtCore import Qt, pyqtSignal

class CommandPalette(QDialog):
    action_selected = pyqtSignal(str)

    def __init__(self, actions, parent=None):
        super().__init__(parent)

        self.actions = actions

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Dialog
        )
        self.setModal(True)
        self.setFixedWidth(500)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search actions...")
        layout.addWidget(self.search_input)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.populate_list()

        self.search_input.textChanged.connect(self.filter_list)
        self.list_widget.itemDoubleClicked.connect(self.select_action)

        self.search_input.setFocus()

    def populate_list(self, items=None):
        self.list_widget.clear()
        items = items or self.actions.keys()
        for name in items:
            QListWidgetItem(name, self.list_widget)

    def filter_list(self, text):
        filtered = [
            name for name in self.actions.keys()
            if text.lower() in name.lower()
        ]
        self.populate_list(filtered)

    def select_action(self, item):
        self.action_selected.emit(item.text())
        self.accept()
