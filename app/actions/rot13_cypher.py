from .base import Action
class Rot13CypherAction(Action):
    name = "Rot 13 Cypher"
    def run(self, text: str) -> str:
        import codecs
        return codecs.encode(text, 'rot_13')

