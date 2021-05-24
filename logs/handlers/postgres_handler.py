from logging import Handler, LogRecord
from logs.models import MessageLog


#TODO: Logging system
class PostgresLogHandler(Handler):
    def emit(self, record: LogRecord) -> None:
        MessageLog.objects.create(level=record.levelname, message=record.msg)
