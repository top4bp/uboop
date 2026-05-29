from .base import Action
import re

class SumAllAction(Action):
    name = "Sum All"
    info = True
    def run(self, text: str) -> str:
        total = sum(int(n) for n in re.findall(r'-?\d+', text))
        return f"Sum = {total}"
