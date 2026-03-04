from .base import Action
class UrlRefangAction(Action):
    name = "URL Refang"
    def run(self, text: str) -> str:
        return text.replace('[.]', '.')

