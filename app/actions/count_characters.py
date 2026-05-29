from .base import Action

class CountCharactersAction(Action):
    name = "Count Characters"
    info = True
    def run(self, text: str) -> str:
        return f"{len(text)} characters"
