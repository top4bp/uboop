from .base import Action
import urllib.parse
class UrlEntitiesDecodeAction(Action):
    name = "URL Entities Decode"
    def run(self, text: str) -> str:
        return urllib.parse.unquote(text)

