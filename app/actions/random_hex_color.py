from .base import Action
import random

class RandomHexColorAction(Action):
    name = "Random Hex Color"
    def run(self, text: str) -> str:
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

