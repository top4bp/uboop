from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QLabel, QFrame
)
from PyQt6.QtCore import Qt, pyqtSignal, QEvent


class CommandPalette(QDialog):
    """Spotlight-style command palette with keyboard-first UX."""

    action_selected = pyqtSignal(str)

    def __init__(self, actions, parent=None):
        super().__init__(parent)

        self.actions = actions

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Dialog
            | Qt.WindowType.NoDropShadowWindowHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setModal(True)
        self.setFixedWidth(560)

        # Outer transparent layout so the inner frame can have rounded corners.
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)

        self.frame = QFrame()
        self.frame.setObjectName("paletteFrame")
        outer.addWidget(self.frame)

        layout = QVBoxLayout(self.frame)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(
            "Type to search actions…  (↑/↓ to navigate, Enter to run, Esc to close)"
        )
        self.search_input.setClearButtonEnabled(True)
        layout.addWidget(self.search_input)

        self.list_widget = QListWidget()
        self.list_widget.setUniformItemSizes(True)
        self.list_widget.setMinimumHeight(320)
        self.list_widget.setMaximumHeight(420)
        self.list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        layout.addWidget(self.list_widget)

        self.status_label = QLabel()
        self.status_label.setObjectName("paletteStatus")
        layout.addWidget(self.status_label)

        self.setStyleSheet(
            """
            QFrame#paletteFrame {
                background-color: #252526;
                border: 1px solid #3c3c3c;
                border-radius: 10px;
            }
            QLineEdit {
                background-color: #1e1e1e;
                color: #f0f0f0;
                border: 1px solid #3c3c3c;
                border-radius: 6px;
                padding: 8px 10px;
                font-size: 14px;
                selection-background-color: #094771;
            }
            QLineEdit:focus {
                border: 1px solid #0a84ff;
            }
            QListWidget {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 1px solid #3c3c3c;
                border-radius: 6px;
                padding: 4px;
                outline: 0;
                font-size: 13px;
            }
            QListWidget::item {
                padding: 6px 8px;
                border-radius: 4px;
            }
            QListWidget::item:selected {
                background-color: #094771;
                color: #ffffff;
            }
            QListWidget::item:hover {
                background-color: #2a2d2e;
            }
            QLabel#paletteStatus {
                color: #888888;
                font-size: 11px;
                padding: 2px 4px 0 4px;
            }
            """
        )

        # Wire up events
        self._all_names = list(self.actions.keys())
        self.search_input.textChanged.connect(self.filter_list)
        self.search_input.returnPressed.connect(self._activate_current)
        self.list_widget.itemActivated.connect(self.select_action)
        self.list_widget.itemDoubleClicked.connect(self.select_action)

        # Forward arrow keys / page nav from the search box to the list.
        self.search_input.installEventFilter(self)

        self.populate_list(self._all_names)
        self.search_input.setFocus()

    # ----- filtering -----------------------------------------------------

    def populate_list(self, items):
        self.list_widget.clear()
        for name in items:
            QListWidgetItem(name, self.list_widget)
        if self.list_widget.count() > 0:
            self.list_widget.setCurrentRow(0)
        total = len(self._all_names)
        shown = self.list_widget.count()
        if shown == 0:
            self.status_label.setText("No matching actions")
        else:
            self.status_label.setText(f"{shown} of {total} actions")

    def filter_list(self, text):
        query = text.strip().lower()
        if not query:
            self.populate_list(self._all_names)
            return

        scored = []
        for name in self._all_names:
            score = self._score(name.lower(), query)
            if score is not None:
                scored.append((score, name))
        scored.sort(key=lambda x: (x[0], x[1].lower()))
        self.populate_list([n for _, n in scored])

    @staticmethod
    def _score(name: str, query: str):
        """Lower is better. Returns None if no match."""
        # 1) Exact substring — strongly preferred.
        idx = name.find(query)
        if idx != -1:
            if idx == 0:
                return 0
            if name[idx - 1] == " ":
                return 1
            return 2 + idx * 0.01

        # 2) Subsequence match (each query char in order).
        i = 0
        positions = []
        for j, ch in enumerate(name):
            if i < len(query) and ch == query[i]:
                positions.append(j)
                i += 1
        if i == len(query):
            spread = positions[-1] - positions[0]
            word_start_bonus = sum(
                1 for p in positions if p == 0 or name[p - 1] == " "
            )
            return 100 + spread - word_start_bonus * 3
        return None

    # ----- key handling --------------------------------------------------

    def eventFilter(self, obj, event):
        if obj is self.search_input and event.type() == QEvent.Type.KeyPress:
            key = event.key()
            nav_keys = (
                Qt.Key.Key_Up, Qt.Key.Key_Down,
                Qt.Key.Key_PageUp, Qt.Key.Key_PageDown,
                Qt.Key.Key_Home, Qt.Key.Key_End,
            )
            if key in nav_keys:
                self.list_widget.keyPressEvent(event)
                return True
        return super().eventFilter(obj, event)

    def _activate_current(self):
        item = self.list_widget.currentItem()
        if item is not None:
            self.select_action(item)

    def select_action(self, item):
        self.action_selected.emit(item.text())
        self.accept()
