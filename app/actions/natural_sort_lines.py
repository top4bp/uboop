from .base import Action
import natsort

class NaturalSortLinesAction(Action):
    name = "Natural Sort Lines"
    def run(self, text: str) -> str:
        lines = text.splitlines()
        return '\n'.join(natsort.natsorted(lines))

