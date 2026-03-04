from .base import Action
class AsciiToHexAction(Action):
    name = "ASCII to Hex"
    def run(self, text: str) -> str:
        return ' '.join(format(ord(c), '02x') for c in text)

