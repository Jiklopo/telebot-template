# Django Telegram Bot

This repository is a template for creating Telegram bot and deploy it to Heroku. You have to follow a few simple steps
to deploy it to Heroku. This bot is based on [Django](https://www.djangoproject.com/)
and [DRF](https://www.django-rest-framework.org/) so you can modify it as a regular django app.

# Heroku Deploy Guide

1. [Create your telegram bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot) and obtain token.
2. Create ___your repo___ from this template.
3. Go and register on https://www.heroku.com/
4. Create an app
    - Go to settings, click reveal config vars
    - Add a variable with the key TOKEN and the value of your bot token
    - Go to deploy, in the deployment method section click GitHub, connect your account
    - Connect the repository you forked on step 2
    - Click "deploy branch" and enable Automatic Deploys
5. Now, you can text your bot and it will echo your message if everything has been set up correctly
6. Edit the bot/bot.py file to [create your own bot.](https://github.com/eternnoir/pyTelegramBotAPI)
7. Push changes to your repo to update your bot.

# Ubuntu setup guide
###### Tested on Ubuntu 20.04.02.
1. Install PyCharm Community: `sudo snap install pycharm-community --classic`.
2. Install packages: `sudo apt install postgresql libpq-dev python3-pip`.
3. Create ___your own___ repository from this template ___if you have not done so already___.
4. [Clone your repo](https://www.jetbrains.com/pycharm/guide/tips/create-project-from-github/) using PyCharm.
5. [Create virtualenv](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env) in PyCharm.
6. [Install the requirements](https://www.jetbrains.com/help/pycharm/managing-dependencies.html#apply_dependencies).
7. Open _botnet/settings.py_ and change the values of USER and PASSWORD ("jiklopo" and "kartop") in the database settings.
8. Configure database (";" in the end is important):
    - Open terminal
    - Start psql: `sudo -u postgres psql`
    - Create database: `CREATE DATABASE telebot;`
    - Connect to the db: `\c telebot`
    - Create User: `CREATE USER YOUR_USER WITH PASSWORD 'YOUR_PASSWORD';` __Don't forget to replace *YOUR_USER* and *YOUR_PASSWORD* to the values from step 4__
    - Exit: `\q`
9. [Create Configuration](https://www.jetbrains.com/help/pycharm/creating-and-editing-run-debug-configurations.html#createExplicitly). Select __manage.py__ file for the __Script path__, __Parameters: runserver__ and create __Environment variable__ TOKEN with the value of your bot token.
10. Now you can start your project using the play button.