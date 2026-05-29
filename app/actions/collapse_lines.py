from .base import Action

class CollapseLinesAction(Action):
    name = "Collapse Lines"
    def run(self, text: str) -> str:
        return " ".join(line.strip() for line in text.splitlines() if line.strip())

