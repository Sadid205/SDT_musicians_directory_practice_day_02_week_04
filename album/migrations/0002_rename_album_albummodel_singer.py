# Generated by Django 5.0.6 on 2024-05-31 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albummodel',
            old_name='Album',
            new_name='Singer',
        ),
    ]
