# Generated by Django 4.0.3 on 2022-04-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0006_checksend_code_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckSendJSON',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_field', models.JSONField()),
            ],
        ),
    ]
