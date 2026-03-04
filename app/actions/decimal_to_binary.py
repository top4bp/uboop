from .base import Action
class DecimalToBinaryAction(Action):
    name = "Decimal to Binary"
    def run(self, text: str) -> str:
        return bin(int(text))[2:]

