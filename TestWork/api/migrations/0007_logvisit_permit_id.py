# Generated by Django 4.2.1 on 2023-05-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_logvisit_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='logvisit',
            name='permit_id',
            field=models.CharField(default=None),
        ),
    ]
