# Generated by Django 4.0.3 on 2022-04-17 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0007_checksendjson'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CheckSendJSON',
        ),
        migrations.RenameField(
            model_name='checksend',
            old_name='code_file',
            new_name='code',
        ),
    ]
