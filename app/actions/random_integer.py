from .base import Action
import random

class RandomIntegerAction(Action):
    name = "Random Integer"
    def run(self, text: str) -> str:
        return str(random.randint(0, 100))

