import logging
from logs.handlers.postgres_handler import PostgresLogHandler
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from bot.bot import bot

logger = logging.getLogger('postgres')
logger.addHandler(PostgresLogHandler())


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['msg'] = 'Salem!'
        return ctx


class MyLoginView(LoginView):
    template_name = 'login.html'


class MyLogoutView(LogoutView):
    template_name = 'login.html'


class ControlView(LoginRequiredMixin, TemplateView):
    template_name = 'control.html'


class SetWebhookView(LoginRequiredMixin, TemplateView):
    template_name = 'webhook.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        try:
            url = self.request.build_absolute_uri()
            i = url.rfind('/')
            bot.remove_webhook()
            bot.set_webhook(f"{url[:i]}/{bot.token}")
            ctx['msg'] = 'Webhook was successfully set!'
        except Exception:
            ctx['msg'] = f'An error occurred. Webhook was not set.'
        return ctx
