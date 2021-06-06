from django.db import models


class BotUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=32)
    active = models.BooleanField(default=True)


class MessageLog(models.Model):
    user = models.ForeignKey('BotUser', on_delete=models.CASCADE)
    private = models.BooleanField()
    timestamp = models.DateTimeField()
    text = models.TextField()


class Log(models.Model):
    level = models.CharField(max_length=24)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    request = models.TextField()
