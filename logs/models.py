from django.db import models


class Log(models.Model):
    level = models.CharField(max_length=24)
    timestamp = models.DateTimeField(auto_created=True)
    message = models.CharField(max_length=256)
