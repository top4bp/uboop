from .base import Action

class DowncaseAction(Action):
    name = "Downcase"
    def run(self, text: str) -> str:
        return text.lower()

