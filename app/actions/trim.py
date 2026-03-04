from .base import Action
class TrimAction(Action):
    name = "Trim"
    def run(self, text: str) -> str:
        return text.strip()

