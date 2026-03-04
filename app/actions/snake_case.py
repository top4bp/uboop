from .base import Action
import re
class SnakeCaseAction(Action):
    name = "Snake Case"
    def run(self, text: str) -> str:
        return '_'.join(re.split(r'[^a-zA-Z0-9]', text)).lower()

