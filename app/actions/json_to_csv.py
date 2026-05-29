from .base import Action
import json
import csv
import io

class JsonToCsvAction(Action):
    name = "JSON to CSV"
    def run(self, text: str) -> str:
        data = json.loads(text)
        if not isinstance(data, list) or not data:
            raise ValueError("JSON must be a non-empty array of objects")
        # Union of keys, preserving first-seen order
        headers = []
        seen = set()
        for row in data:
            if not isinstance(row, dict):
                raise ValueError("Each item must be an object")
            for k in row.keys():
                if k not in seen:
                    seen.add(k)
                    headers.append(k)
        out = io.StringIO()
        writer = csv.DictWriter(out, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow({k: row.get(k, "") for k in headers})
        return out.getvalue().rstrip("\r\n")

