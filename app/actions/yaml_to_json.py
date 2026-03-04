from .base import Action
import json, yaml
class YamlToJsonAction(Action):
    name = "YAML to JSON"
    def run(self, text: str) -> str:
        return json.dumps(yaml.safe_load(text), indent=2)

