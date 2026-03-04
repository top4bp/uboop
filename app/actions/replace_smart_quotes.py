from .base import Action
class ReplaceSmartQuotesAction(Action):
    name = "Replace Smart Quotes"
    def run(self, text: str) -> str:
        return text.replace('“','').replace('”','').replace('‘','').replace('’','')

