from .base import Action
import hashlib
class Sha256HashAction(Action):
    name = "SHA256 hash"
    def run(self, text: str) -> str:
        return hashlib.sha256(text.encode()).hexdigest()

