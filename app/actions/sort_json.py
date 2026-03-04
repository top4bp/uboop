from .base import Action
import json
class SortJsonAction(Action):
    name = "Sort JSON"
    def run(self, text: str) -> str:
        return json.dumps(json.loads(text), indent=2)

