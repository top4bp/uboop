from .base import Action
import re
class KebabCaseAction(Action):
    name = "Kebab Case"
    def run(self, text: str) -> str:
        return '-'.join(re.split(r'[^a-zA-Z0-9]', text)).lower()

