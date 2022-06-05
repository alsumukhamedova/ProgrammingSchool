# Generated by Django 4.0.3 on 2022-05-19 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0014_marks_alter_checksend_user_id_tasks_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_lang', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=7)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_client.tasks')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_client.users')),
            ],
        ),
        migrations.DeleteModel(
            name='ResultSend',
        ),
    ]
