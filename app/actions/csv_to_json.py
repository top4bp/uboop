from .base import Action
import json
import csv
import io

class CsvToJsonAction(Action):
    name = "CSV to JSON"
    def run(self, text: str) -> str:
        reader = csv.DictReader(io.StringIO(text))
        rows = [dict(r) for r in reader]
        return json.dumps(rows, indent=2, ensure_ascii=False)

