# Generated by Django 2.2.5 on 2019-11-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startPolling', '0003_auto_20191114_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]