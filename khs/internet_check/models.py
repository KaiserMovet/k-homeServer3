from django.db import models

# Create your models here.


class InternetStatus(models.Model):
    change_time = models.DateTimeField()
    status = models.BooleanField()


class InternetSpeed(models.Model):
    date = models.DateTimeField()
    upload = models.FloatField()
    download = models.FloatField()
