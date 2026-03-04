from .base import Action
import json, yaml
class JsonToYamlAction(Action):
    name = "JSON to YAML"
    def run(self, text: str) -> str:
        return yaml.dump(json.loads(text))

