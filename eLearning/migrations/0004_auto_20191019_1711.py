# Generated by Django 2.0.2 on 2019-10-19 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eLearning', '0003_auto_20191019_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursetutorial',
            name='series_title',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='coursetutorial',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 17, 11, 17, 191407)),
        ),
        migrations.AlterField(
            model_name='document',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 17, 11, 17, 195396)),
        ),
        migrations.AlterField(
            model_name='video',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 17, 11, 17, 185426)),
        ),
    ]
