# Generated by Django 4.0.3 on 2022-05-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0023_alter_studentgroupinfo_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markedtasks',
            name='task_assigment_time',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='markedtasks',
            name='time_solve_task',
            field=models.IntegerField(default=1),
        ),
    ]