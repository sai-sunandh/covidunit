# Generated by Django 3.1 on 2020-09-12 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covidtest', '0003_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='Age',
        ),
    ]
