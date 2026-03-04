from .base import Action
class BinaryToDecimalAction(Action):
    name = "Binary to Decimal"
    def run(self, text: str) -> str:
        return str(int(text, 2))

