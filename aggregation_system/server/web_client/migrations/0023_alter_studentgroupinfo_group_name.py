# Generated by Django 4.0.3 on 2022-05-24 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0022_alter_checksend_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroupinfo',
            name='group_name',
            field=models.CharField(default='0', max_length=50, unique=True),
        ),
    ]