from django.urls import path
from interface.views import *

urlpatterns = [
    path('', ControlsView.as_view(), name='controls'),
    path('login', MyLoginView.as_view(), name='login'),
    path('change_password', PasswordChangeView.as_view(), name='change_password'),
    path('set_webhook', SetWebhookView.as_view(), name='set_webhook'),
]
