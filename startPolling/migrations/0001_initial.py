# Generated by Django 2.2.5 on 2019-11-18 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuestionText', models.CharField(max_length=500)),
                ('Description', models.TextField(blank=True)),
                ('CreationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('IsAllowComments', models.BooleanField(help_text='Allow comments on user submissions.', null=True)),
                ('IsPrivate', models.BooleanField(default=False)),
                ('IsMultiple', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Votes', models.IntegerField(default=0)),
                ('IP', models.CharField(blank=True, max_length=30)),
                ('ChoiceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startPolling.Choice')),
                ('QuestionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startPolling.Question')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startPolling.Question'),
        ),
    ]
