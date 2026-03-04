from .base import Action
import hashlib
class Sha512HashAction(Action):
    name = "SHA512 hash"
    def run(self, text: str) -> str:
        return hashlib.sha512(text.encode()).hexdigest()

