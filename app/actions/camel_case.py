from .base import Action
import re
class CamelCaseAction(Action):
    name = "Camel Case"
    def run(self, text: str) -> str:
        words = re.split(r'[^a-zA-Z0-9]', text)
        return words[0].lower() + ''.join(w.title() for w in words[1:])

