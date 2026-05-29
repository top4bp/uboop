from .base import Action

class AddSlashesAction(Action):
    name = "Add Slashes"
    def run(self, text: str) -> str:
        # Escape quotes, backslashes, and NUL
        out = []
        for ch in text:
            if ch in ("\\", "'", '"'):
                out.append("\\" + ch)
            elif ch == "\0":
                out.append("\\0")
            else:
                out.append(ch)
        return "".join(out)

