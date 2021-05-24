from logging import Handler, LogRecord
from logs.models import Log


class PostgresHandler(Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record: LogRecord) -> None:
        Log.objects.create(level=record.levelname, message=record.message)
