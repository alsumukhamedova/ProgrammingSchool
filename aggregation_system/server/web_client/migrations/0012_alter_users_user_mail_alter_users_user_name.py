# Generated by Django 4.0.3 on 2022-05-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0011_users_user_mail_users_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_mail',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]