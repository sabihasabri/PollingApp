# Generated by Django 2.2.5 on 2019-11-19 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startPolling', '0003_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CommentField', models.CharField(blank=True, max_length=5000, null=True)),
                ('QID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startPolling.Question')),
            ],
        ),
    ]
