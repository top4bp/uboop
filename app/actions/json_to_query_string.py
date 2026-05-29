from .base import Action
import json
import urllib.parse

class JsonToQueryStringAction(Action):
    name = "JSON to Query String"
    def run(self, text: str) -> str:
        data = json.loads(text)
        if not isinstance(data, dict):
            raise ValueError("JSON root must be an object")
        # Flatten lists into repeated keys
        pairs = []
        for k, v in data.items():
            if isinstance(v, list):
                for item in v:
                    pairs.append((k, str(item)))
            else:
                pairs.append((k, str(v)))
        return urllib.parse.urlencode(pairs)

