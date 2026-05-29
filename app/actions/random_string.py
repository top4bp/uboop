from .base import Action
import random
import string

class RandomStringAction(Action):
    name = "Random String"
    def run(self, text: str) -> str:
        alphabet = string.ascii_letters + string.digits
        return "".join(random.choice(alphabet) for _ in range(32))

