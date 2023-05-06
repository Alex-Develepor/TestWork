import django.utils.timezone
from django.db import models


class UserOS(models.Model):
    login = models.CharField(primary_key=True)
    time_detection = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


class Gate(models.Model):
    num_chekpoint = models.CharField(primary_key=True)
    time_of_work_until = models.DateTimeField(default=django.utils.timezone.now)


class LogVisit(models.Model):
    user = models.CharField()
    status = models.BooleanField(default=False)
    num_checkpoint = models.CharField()
    permit_id = models.CharField()
    time_detection = models.DateTimeField(auto_now_add=True)
