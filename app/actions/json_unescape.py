from .base import Action
import json

class JsonUnescapeAction(Action):
    name = "JSON Unescape"
    def run(self, text: str) -> str:
        # Wrap in quotes if needed, then decode
        t = text
        if not (t.startswith('"') and t.endswith('"')):
            t = '"' + t + '"'
        return json.loads(t)

