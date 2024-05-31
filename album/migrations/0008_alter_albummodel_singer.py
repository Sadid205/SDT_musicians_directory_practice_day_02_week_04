# Generated by Django 5.0.6 on 2024-05-31 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0007_alter_albummodel_albumname_alter_albummodel_rating'),
        ('musician', '0002_alter_musicianmodel_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='Singer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musician.musicianmodel'),
        ),
    ]