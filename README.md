# Django Telegram Bot

This repository is a template for creating Telegram bot and deploy it to Heroku. You have to follow a few simple steps
to deploy it to Heroku. This bot is based on [Django](https://www.djangoproject.com/)
and [DRF](https://www.django-rest-framework.org/) so you can modify at as a regular django app.

# Setup Guide

1. [Create your telegram bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot) and obtain token.
2. Fork this repo.
3. Go and register on https://www.heroku.com/
4. Create an app
    - Go to settings, click reveal config vars
    - Add a variable TOKEN with the value of your bot token, e.g. 1202834947:AAFQ7YUBNAaH4_pCK8lHZSHZyGqW8B0YkW4
    - Add a variable APP_URL which is the url of your app without "/" in the end,
      e.g. https://application_name.herokuapp.com
    - Go to deploy, in the deployment method section click GitHub, connect your account
    - Connect the repository you forked on step 2
    - Click "deploy branch" and enable Automatic Deploys
5. Now, you can text your bot and it will echo your message if everything has been set up correctly
6. Edit the bot/bot.py file to [create your own bot.](https://github.com/eternnoir/pyTelegramBotAPI)
7. Push changes to your repo for them to take effect.
