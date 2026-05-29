from .base import Action

class RemoveDuplicateLinesAction(Action):
    name = "Remove Duplicate Lines"
    def run(self, text: str) -> str:
        seen = set()
        out = []
        for line in text.splitlines():
            if line not in seen:
                seen.add(line)
                out.append(line)
        return "\n".join(out)

