# Generated by Django 3.2.4 on 2021-09-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0006_auto_20210808_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='meeting_url',
            field=models.URLField(null=True),
        ),
    ]
