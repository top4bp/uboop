from .base import Action

class MarkdownQuoteAction(Action):
    name = "Markdown Quote"
    def run(self, text: str) -> str:
        return "\n".join(("> " + line) if line else ">" for line in text.splitlines())

