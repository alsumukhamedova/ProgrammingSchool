# Generated by Django 3.2.9 on 2021-12-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0004_auto_20211213_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checksend',
            name='program_lang',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='resultsend',
            name='program_lang',
            field=models.CharField(max_length=30),
        ),
    ]