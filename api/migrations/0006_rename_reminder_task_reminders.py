# Generated by Django 4.1.2 on 2022-11-03 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_task_date_task_reminder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='reminder',
            new_name='reminders',
        ),
    ]
