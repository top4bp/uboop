from .base import Action
class SpongeCaseAction(Action):
    name = "SpONGeCASe"
    def run(self, text: str) -> str:
        return ''.join(c.upper() if i%2 else c.lower() for i,c in enumerate(text))

