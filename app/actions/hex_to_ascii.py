from .base import Action
class HexToAsciiAction(Action):
    name = "Hex to ASCII"
    def run(self, text: str) -> str:
        return bytes.fromhex(text.replace(' ', '')).decode('utf-8')

