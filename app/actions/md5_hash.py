from .base import Action
import hashlib

class Md5HashAction(Action):
    name = "MD5 Hash"
    def run(self, text: str) -> str:
        return hashlib.md5(text.encode("utf-8")).hexdigest()

