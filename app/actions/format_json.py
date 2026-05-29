from .base import Action
import json

class FormatJsonAction(Action):
    name = "Format JSON"
    def run(self, text: str) -> str:
        return json.dumps(json.loads(text), indent=2, sort_keys=False, ensure_ascii=False)

