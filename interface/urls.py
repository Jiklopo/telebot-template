from django.urls import path
from interface.views import *

urlpatterns = [
    path('controls', ControlView.as_view(), name='controls'),
    path('', IndexView.as_view(), name='index'),
    path('set-webhook', SetWebhookView.as_view(), name='set-webhook'),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', MyLogoutView.as_view(), name='logout'),
]
