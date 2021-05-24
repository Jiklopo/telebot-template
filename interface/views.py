import logging
from logs.postgres_handler import PostgresHandler
from django.views.generic import TemplateView

logger = logging.getLogger('postgres')
logger.addHandler(PostgresHandler())

class ControlView(TemplateView):
    template_name = 'control.html'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['msg'] = 'Salem!'
        return ctx
