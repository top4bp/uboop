from .base import Action

class ReverseStringAction(Action):
    name = "Reverse String"
    def run(self, text: str) -> str:
        return text[::-1]

