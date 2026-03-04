from .base import Action
import base64, json
class JwtDecodeAction(Action):
    name = "JWT Decode"
    def run(self, text: str) -> str:
        parts = text.split('.')
        if len(parts) != 3: return 'Invalid JWT'
        payload = parts[1] + '=='
        return json.dumps(json.loads(base64.urlsafe_b64decode(payload)), indent=2)

