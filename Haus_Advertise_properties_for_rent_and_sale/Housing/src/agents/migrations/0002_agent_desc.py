# Generated by Django 3.1 on 2020-10-30 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='desc',
            field=models.CharField(default='', max_length=60),
        ),
    ]