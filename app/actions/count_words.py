from .base import Action
class CountWordsAction(Action):
    name = "Count Words"
    def run(self, text: str) -> str:
        return str(len(text.split()))

