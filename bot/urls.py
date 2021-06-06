from django.urls import path
from bot.views import bot_update_handler
from bot.bot import TOKEN

urlpatterns = [
    path(TOKEN or 'a', bot_update_handler, name='bot_update_handler')
]
