from django.urls import path

from bot.views import webhook

urlpatterns = [
    path('<token>', webhook, name='webhook')
]
