# Generated by Django 3.1.1 on 2020-09-27 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_property_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
