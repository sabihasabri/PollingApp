# Generated by Django 2.2.5 on 2019-11-14 06:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500)),
                ('date', models.DateTimeField(verbose_name='created on')),
                ('description', models.TextField(blank=True)),
                ('starts_at', models.DateTimeField(default=datetime.datetime.now)),
                ('ends_at', models.DateTimeField(blank=True, null=True)),
                ('allow_comments', models.BooleanField(default=False, help_text='Allow comments on user submissions.')),
                ('is_private', models.BooleanField(default=False)),
                ('allow_multiple', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startPolling.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startPolling.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startPolling.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startPolling.Question')),
                ('voted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('question', 'voted_by')},
            },
        ),
    ]
