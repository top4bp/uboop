from .base import Action
import json, urllib.parse
class QueryStringToJsonAction(Action):
    name = "Query String to JSON"
    def run(self, text: str) -> str:
        return json.dumps(dict(urllib.parse.parse_qsl(text)))

