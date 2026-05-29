from .base import Action
import base64

class Base64EncodeAction(Action):
    name = "Base64 Encode"
    def run(self, text: str) -> str:
        return base64.b64encode(text.encode("utf-8")).decode("ascii")

