import importlib
from logging import Handler, LogRecord


class PostgresLogHandler(Handler):
    def __init__(self, level='ERROR'):
        super().__init__(level)
        self.log_model = None

    def emit(self, record: LogRecord) -> None:
        if not self.log_model:
            self.log_model = importlib.import_module('logs.models').Log
        if hasattr(record, 'request'):
            request = ''
        else:
            request = record.request.body

        self.log_model.objects.create(
            level=record.levelname,
            message=record.message,
            request=request)

