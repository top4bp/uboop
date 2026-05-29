from .base import Action
import html

class HtmlDecodeAction(Action):
    name = "HTML Decode"
    def run(self, text: str) -> str:
        return html.unescape(text)

