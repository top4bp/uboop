from .base import Action
import json
class MinifyJsonAction(Action):
    name = "Minify JSON"
    def run(self, text: str) -> str:
        return json.dumps(json.loads(text), separators=(',', ':'))

