from .base import Action
import base64

class Base64DecodeAction(Action):
    name = "Base64 Decode"
    def run(self, text: str) -> str:
        # Pad if necessary
        data = text.strip()
        padding = (-len(data)) % 4
        data += "=" * padding
        return base64.b64decode(data).decode("utf-8", errors="replace")

