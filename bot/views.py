import logging

import telebot
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.views import Response
from bot.bot import bot

logger = logging.getLogger(__name__)


@api_view(['GET'])
def set_webhook(request):
    try:
        url = reverse('webhook-handle')
        url = request.build_absolute_uri(url)
        bot.remove_webhook()
        bot.set_webhook(url)
        logger.info(f'Webhook was set to:{url}')
        return Response('Webhook was successfully set.')
    except Exception as e:
        logger.exception('Error while setting webhook.')
        return Response(str(e))


@api_view(['POST'])
def handle_webhook(request):
    logger.info(request.data)
    bot.process_new_updates([telebot.types.Update.de_json(request.data)])
    return Response('!')
