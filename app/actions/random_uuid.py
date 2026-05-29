from .base import Action
import uuid

class UuidGenerateAction(Action):
    name = "Random UUID"
    def run(self, text: str) -> str:
        return str(uuid.uuid4())

