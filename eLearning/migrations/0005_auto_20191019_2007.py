# Generated by Django 2.0.2 on 2019-10-19 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eLearning', '0004_auto_20191019_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='tag',
            new_name='tags',
        ),
        migrations.AddField(
            model_name='material',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='choice_materials', to='eLearning.Tag'),
        ),
        migrations.AddField(
            model_name='material',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 20, 7, 41, 208610)),
        ),
        migrations.AlterField(
            model_name='coursetutorial',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 20, 7, 41, 211593)),
        ),
        migrations.AlterField(
            model_name='document',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 20, 7, 41, 218624)),
        ),
        migrations.AlterField(
            model_name='video',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 20, 7, 41, 203578)),
        ),
    ]
