# Generated by Django 5.0.6 on 2024-05-31 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicianmodel',
            name='FirstName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='musicianmodel',
            name='InstrumentType',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='musicianmodel',
            name='LastName',
            field=models.CharField(max_length=50),
        ),
    ]
