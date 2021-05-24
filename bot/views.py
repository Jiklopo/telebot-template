import logging
import telebot
from rest_framework.decorators import api_view
from rest_framework.views import Response
from bot.bot import bot
from logs.postgres_handler import PostgresHandler

logger = logging.getLogger('postgres')
logger.addHandler(PostgresHandler())


@api_view(['GET', 'POST'])
def webhook(request, token):
    if request.method == 'GET':
        try:
            url = request.build_absolute_uri()
            i = url.rfind('/')
            bot.remove_webhook()
            bot.set_webhook(f"{url[:i]}/{token}")
            return Response('Webhook was successfully set.')
        except Exception as e:
            return Response(str(e))

    elif request.method == 'POST':
        bot.process_new_updates([telebot.types.Update.de_json(request.data)])
        print(request.data)
        return Response('!')
