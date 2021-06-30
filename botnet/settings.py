from os import getenv
from pathlib import Path
import dotenv
import dj_database_url
import django_heroku

dotenv.load_dotenv()
ENV = getenv('ENV')
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = getenv('TOKEN') or 'very_secret_key'
DEBUG = ENV == 'DEV'
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bot',
    'logs',
    'interface',

    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'botnet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },

        'postgres': {
            'class': 'logs.handlers.postgres_handler.PostgresLogHandler',
            'level': 'WARNING',
        },
    },
    'root': {
        'handlers': ['console', 'postgres'],
        'level': 'INFO',
    },
}

WSGI_APPLICATION = 'botnet.wsgi.application'

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=None)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'controls'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles/')

if ENV != 'DEV':
    django_heroku.settings(locals(), logging=False)
