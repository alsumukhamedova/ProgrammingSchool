# Generated by Django 4.0.3 on 2022-06-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0024_alter_markedtasks_task_assigment_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='time_to_solve',
            field=models.CharField(max_length=200),
        ),
    ]
