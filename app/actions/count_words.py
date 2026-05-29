from .base import Action

class CountWordsAction(Action):
    name = "Count Words"
    info = True
    def run(self, text: str) -> str:
        return f"{len(text.split())} words"
