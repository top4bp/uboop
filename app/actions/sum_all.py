from .base import Action
import re
class SumAllAction(Action):
    name = "Sum All"
    def run(self, text: str) -> str:
        return str(sum(int(n) for n in re.findall(r'-?\d+', text)))

