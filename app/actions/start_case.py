from .base import Action
class StartCaseAction(Action):
    name = "Start Case"
    def run(self, text: str) -> str:
        return text.title()

