from .base import Action
import hashlib
class Sha1HashAction(Action):
    name = "SHA1 hash"
    def run(self, text: str) -> str:
        return hashlib.sha1(text.encode()).hexdigest()

