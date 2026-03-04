from .base import Action
class FormatSqlAction(Action):
    name = "Format SQL"
    def run(self, text: str) -> str:
        # TODO: format SQL
        return text

