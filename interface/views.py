from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse
from bot.bot import bot
from logs.models import Log

class ControlsView(LoginRequiredMixin, TemplateView):
    template_name = 'bot/controls.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['logs'] = Log.objects.order_by('timestamp')[:10]
        return ctx



class MyLoginView(LoginView):
    template_name = 'auth/login.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'auth/password_change.html'


class SetWebhookView(LoginRequiredMixin, TemplateView):
    template_name = 'bot/webhook.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        url = self.request.build_absolute_uri(reverse('bot_update_handler'))
        bot.remove_webhook()
        bot.set_webhook(url)
        ctx['msg'] = 'Webhook was successfully set!'
        return ctx
