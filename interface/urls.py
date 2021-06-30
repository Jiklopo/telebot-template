from django.urls import path
from interface.views import *

urlpatterns = [
    path('', ControlsView.as_view(), name='controls'),
    path('set_webhook', SetWebhookView.as_view(), name='set_webhook'),
]
