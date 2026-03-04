from .base import Action
class HexColorToRgbAction(Action):
    name = "Hex Color to RGB"
    def run(self, text: str) -> str:
        t = text.lstrip('#')
        return f"rgb({int(t[0:2],16)}, {int(t[2:4],16)}, {int(t[4:6],16)})" if len(t)==6 else text

