# Generated by Django 3.0.5 on 2020-04-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0003_auto_20200409_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
