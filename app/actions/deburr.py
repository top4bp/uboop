from .base import Action
import unicodedata
class DeburrAction(Action):
    name = "Deburr"
    def run(self, text: str) -> str:
        return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

