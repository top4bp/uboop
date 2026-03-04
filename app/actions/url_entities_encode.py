from .base import Action
import urllib.parse
class UrlEntitiesEncodeAction(Action):
    name = "URL Entities Encode"
    def run(self, text: str) -> str:
        return urllib.parse.quote(text)

