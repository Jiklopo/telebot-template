from django.urls import path, include

from bot.views import set_webhook, handle_webhook
from config.settings import BOT_TOKEN

webhooks = [
    path('', set_webhook, name='webhook-set'),
    path(f'{BOT_TOKEN}/', handle_webhook, name='webhook-handle')
]

urlpatterns = [
    path('webhook/', include(webhooks))
]
