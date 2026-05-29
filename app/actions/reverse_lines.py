from .base import Action

class ReverseLinesAction(Action):
    name = "Reverse Lines"
    def run(self, text: str) -> str:
        return "\n".join(reversed(text.splitlines()))

