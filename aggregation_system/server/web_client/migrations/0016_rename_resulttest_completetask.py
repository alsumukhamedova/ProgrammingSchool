# Generated by Django 4.0.3 on 2022-05-19 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0015_resulttest_delete_resultsend'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ResultTest',
            new_name='CompleteTask',
        ),
    ]
