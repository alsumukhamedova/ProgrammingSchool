# Generated by Django 4.0.3 on 2022-05-11 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0010_alter_usertypes_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_login', models.CharField(max_length=50, unique=True)),
                ('user_password', models.CharField(max_length=50)),
                (
                'user_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_client.usertypes')),
                ('user_mail', models.CharField(max_length=50, null=True, unique=True)),
                ('user_name', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
