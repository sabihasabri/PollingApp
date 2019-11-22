# Generated by Django 2.2.5 on 2019-11-19 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startPolling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='ChoiceId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='startPolling.Choice'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='IP',
            field=models.GenericIPAddressField(),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CommentField', models.CharField(blank=True, max_length=5000, null=True)),
                ('Date', models.DateTimeField(auto_now_add=True, null=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_set', to='startPolling.Comment')),
            ],
        ),
    ]