# Generated by Django 4.0.3 on 2022-05-24 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0021_rename_group_groupcomposition_group_id_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='checksend',
            unique_together={('user_id', 'task_id')},
        ),
        migrations.RemoveField(
            model_name='checksend',
            name='testing_stage',
        ),
    ]
