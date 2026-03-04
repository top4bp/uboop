from .base import Action
class DecimalToHexAction(Action):
    name = "Decimal to Hex"
    def run(self, text: str) -> str:
        return hex(int(text))[2:]

