# Django Telegram Bot

This repository is a template for creating Telegram bot and deploy it to Heroku. You have to follow a few simple steps
to deploy it to Heroku. This bot is based on [Django](https://www.djangoproject.com/)
and [DRF](https://www.django-rest-framework.org/) so you can modify it as a regular django app.

# Heroku Deploy Guide

1. [Create your telegram bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot) and obtain token.
2. Create your repo from this template.
3. Go and register on https://www.heroku.com/
4. Create an app
    - Go to settings, click reveal config vars
    - Add a variable with the key TOKEN and the value of your bot token
    - Add a variable with the key APP_URL with the value https://your_app_name.herokuapp.com **Don't forget to replace your_app_name with the actual name of your app!**
    - Go to deploy, in the deployment method section click GitHub, connect your account
    - Connect the repository you forked on step 2
    - Click "deploy branch" and enable Automatic Deploys
5. Now, you can text your bot and it will echo your message if everything has been set up correctly
6. Edit the bot/bot.py file to [create your own bot.](https://github.com/eternnoir/pyTelegramBotAPI)
7. Push changes to your repo for them to take effect.
