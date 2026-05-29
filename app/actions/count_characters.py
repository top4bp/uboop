from .base import Action

class CountCharactersAction(Action):
    name = "Count Characters"
    def run(self, text: str) -> str:
        return str(len(text))

