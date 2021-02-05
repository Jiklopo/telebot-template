import os
import telebot
from rest_framework.decorators import api_view
from rest_framework.views import Response
from bot.bot import bot


@api_view(['GET', 'POST'])
def webhook(request, token):
    if request.method == 'GET':
        try:
            bot.remove_webhook()
            bot.set_webhook(f"{os.getenv('APP_URL')}/{token}")
            return Response('Webhook was successfully set.')
        except Exception as e:
            return Response(str(e))

    elif request.method == 'POST':
        bot.process_new_updates([telebot.types.Update.de_json(request.data)])
        return Response('!')
