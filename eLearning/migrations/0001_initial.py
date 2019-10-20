# Generated by Django 2.0.2 on 2019-10-19 10:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseTutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_tutorials', to='eLearning.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('short_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DocType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docType', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('filename', models.CharField(max_length=1000)),
                ('uploaded_at', models.DateTimeField(default=datetime.datetime(2019, 10, 19, 15, 47, 9, 390677))),
                ('approved', models.BooleanField(default=False)),
                ('course', models.ManyToManyField(blank=True, null=True, related_name='choice_docs', to='eLearning.Course')),
                ('dept', models.ManyToManyField(blank=True, null=True, related_name='choice_docs', to='eLearning.Department')),
                ('doc_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='choice_docs', to='eLearning.DocType')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25555)),
                ('met', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('link', models.CharField(blank=True, max_length=50000, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('uploaded_at', models.DateTimeField(default=datetime.datetime(2019, 10, 19, 15, 47, 9, 375716))),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice_videos', to='eLearning.Course')),
                ('tag', models.ManyToManyField(blank=True, null=True, related_name='choice_videos', to='eLearning.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='sem',
            field=models.ManyToManyField(blank=True, null=True, related_name='choice_docs', to='eLearning.Semester'),
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='choice_docs', to='eLearning.Tag'),
        ),
        migrations.AddField(
            model_name='document',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='choice_docs', to='eLearning.Student'),
        ),
        migrations.AddField(
            model_name='coursetutorial',
            name='materials',
            field=models.ManyToManyField(blank=True, null=True, related_name='choice_courses', to='eLearning.Material'),
        ),
        migrations.AddField(
            model_name='coursetutorial',
            name='uploaded_by_club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice_courses', to='eLearning.Club'),
        ),
        migrations.AddField(
            model_name='coursetutorial',
            name='uploaded_by_dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice_courses', to='eLearning.Department'),
        ),
        migrations.AddField(
            model_name='coursetutorial',
            name='videos',
            field=models.ManyToManyField(blank=True, null=True, related_name='choice_courses', to='eLearning.Video'),
        ),
    ]
