# Generated by Django 3.2.4 on 2021-08-07 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0004_auto_20210807_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='rescheduled_by_doctor',
            new_name='rescheduled_by_consultant',
        ),
    ]