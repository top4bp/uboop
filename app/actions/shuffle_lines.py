from .base import Action
import random
class ShuffleLinesAction(Action):
    name = "Shuffle Lines"
    def run(self, text: str) -> str:
        lines = text.splitlines()
        random.shuffle(lines)
        return '\n'.join(lines)

