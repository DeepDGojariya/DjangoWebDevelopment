# Generated by Django 3.0.5 on 2020-04-12 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'about us', 'verbose_name_plural': 'about us'},
        ),
        migrations.AlterModelOptions(
            name='chef',
            options={'verbose_name': 'chef', 'verbose_name_plural': 'chef'},
        ),
        migrations.AlterModelOptions(
            name='whychooseus',
            options={'verbose_name': 'why choose us', 'verbose_name_plural': 'why choose us'},
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='img',
        ),
    ]