import logging
import telebot
from rest_framework.decorators import api_view
from rest_framework.views import Response
from bot.bot import bot

logger = logging.getLogger('root')


@api_view(['POST'])
def bot_update_handler(request):
    logger.info(request.data)
    bot.process_new_updates([telebot.types.Update.de_json(request.data)])
    return Response('!')
