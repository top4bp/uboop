from .base import Action

class UpcaseAction(Action):
    name = "Upcase"
    def run(self, text: str) -> str:
        return text.upper()

