from __future__ import absolute_import, unicode_literals
from celery.task import periodic_task
from celery.schedules import crontab
from . import models
import os


@periodic_task(run_every=crontab(minute='*/5'), name='chek_user_in_os')
def chek_user_in_os():
    mycmd = 'cut -d: -f1 /etc/passwd > tetx.txt'
    os.system(mycmd)
    list_users = models.UserOS.objects.all().values('login')
    res1 = []
    for obj in list(list_users):
        for _, val in obj.items():
            res1.append(val)

    with open('tetx.txt', 'r') as f:
        for name in f.readlines()[10:]:
            if name.strip() not in res1:
                models.UserOS.objects.create(login=name.strip())
