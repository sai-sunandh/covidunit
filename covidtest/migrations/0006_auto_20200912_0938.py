# Generated by Django 3.1 on 2020-09-12 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidtest', '0005_auto_20200912_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='aches_and_pains',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='chestpain',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='conjunctivitis',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='diarrhoea',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='difficult_breathing',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='dry_cough',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='fever',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='headaches',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='loss_of_speech',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='loss_of_taste',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='rash_on_skin',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='sore_throat',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='tiredness',
            field=models.CharField(max_length=30),
        ),
    ]
