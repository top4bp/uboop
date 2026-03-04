from .base import Action
class MinifyCssAction(Action):
    name = "Minify CSS"
    def run(self, text: str) -> str:
        # TODO: minify CSS
        return text

