from django.db import models


class UserOS(models.Model):
    login = models.CharField(primary_key=True)
    time_detection = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


class Gate(models.Model):
    num_chekpoint = models.CharField(primary_key=True)


class LogVisit(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.CharField()
    status = models.BooleanField()
    num_checkpoint = models.CharField()
    permit_id = models.CharField(default=None)
    time_detection = models.DateTimeField(auto_now_add=True)
