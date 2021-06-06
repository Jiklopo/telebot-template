import logging
from logs.handlers.postgres_handler import PostgresLogHandler
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse
from bot.bot import bot

logger = logging.getLogger('postgres')
logger.addHandler(PostgresLogHandler())


class ControlsView(LoginRequiredMixin, TemplateView):
    template_name = 'bot/controls.html'


class MyLoginView(LoginView):
    template_name = 'auth/login.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'auth/password_change.html'


class SetWebhookView(LoginRequiredMixin, TemplateView):
    template_name = 'bot/webhook.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        try:
            url = self.request.build_absolute_uri(reverse('bot_update_handler'))
            bot.remove_webhook()
            bot.set_webhook(url)
            ctx['msg'] = 'Webhook was successfully set!'
        except Exception:
            ctx['msg'] = f'An error occurred. Webhook was not set.'
        return ctx
