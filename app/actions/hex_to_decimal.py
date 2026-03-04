from .base import Action
class HexToDecimalAction(Action):
    name = "Hex to Decimal"
    def run(self, text: str) -> str:
        return str(int(text, 16))

