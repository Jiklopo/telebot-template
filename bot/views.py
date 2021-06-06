import logging
import telebot
from rest_framework.decorators import api_view
from rest_framework.views import Response
from bot.bot import bot
from logs.handlers.postgres_handler import PostgresLogHandler

logger = logging.getLogger('postgres')
logger.addHandler(PostgresLogHandler())


@api_view(['POST'])
def bot_update_handler(request):
    bot.process_new_updates([telebot.types.Update.de_json(request.data)])
    print(request.data)
    return Response('!')
