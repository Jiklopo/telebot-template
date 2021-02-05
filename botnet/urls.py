from django.contrib import admin
from django.urls import path, include
from os import getenv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bot.urls'))
]
