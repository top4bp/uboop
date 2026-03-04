from .base import Action
class LoremIpsumAction(Action):
    name = "Lorem Ipsum"
    def run(self, text: str) -> str:
        return 'Lorem ipsum dolor sit amet.'

