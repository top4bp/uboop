from .base import Action

class JsonEscapeAction(Action):
    name = "JSON Escape"
    def run(self, text: str) -> str:
        import json
        # Produce an escaped JSON string (without surrounding quotes)
        return json.dumps(text)[1:-1]

