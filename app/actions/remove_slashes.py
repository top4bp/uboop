from .base import Action
import re

class RemoveSlashesAction(Action):
    name = "Remove Slashes"
    def run(self, text: str) -> str:
        # Reverse of Add Slashes: unescape \\, \', \", \0
        def repl(m):
            c = m.group(1)
            if c == "0":
                return "\0"
            return c
        return re.sub(r"\\(.)", repl, text)

