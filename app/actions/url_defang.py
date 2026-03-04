from .base import Action
class UrlDefangAction(Action):
    name = "URL Defang"
    def run(self, text: str) -> str:
        return text.replace('.', '[.]')

