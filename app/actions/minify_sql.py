from .base import Action
class MinifySqlAction(Action):
    name = "Minify SQL"
    def run(self, text: str) -> str:
        # TODO: minify SQL
        return text

