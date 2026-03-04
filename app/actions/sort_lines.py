from .base import Action
class SortLinesAction(Action):
    name = "Sort Lines"
    def run(self, text: str) -> str:
        return '\n'.join(sorted(text.splitlines()))

