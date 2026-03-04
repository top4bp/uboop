from .base import Action
import datetime
class DateToTimestampAction(Action):
    name = "Date to Timestamp"
    def run(self, text: str) -> str:
        dt = datetime.datetime.fromisoformat(text)
        return str(int(dt.timestamp()))

