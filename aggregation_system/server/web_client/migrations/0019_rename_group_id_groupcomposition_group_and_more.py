# Generated by Django 4.0.3 on 2022-05-24 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0018_studentgroupinfo_group_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupcomposition',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='groupcomposition',
            old_name='student_id',
            new_name='student',
        ),
    ]