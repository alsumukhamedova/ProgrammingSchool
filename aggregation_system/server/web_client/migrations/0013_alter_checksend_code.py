# Generated by Django 4.0.3 on 2022-05-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0012_alter_users_user_mail_alter_users_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checksend',
            name='code',
            field=models.TextField(),
        ),
    ]