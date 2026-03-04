from .base import Action
import html
class HtmlEncodeAction(Action):
    name = "HTML Encode all Characters"
    def run(self, text: str) -> str:
        return html.escape(text)

