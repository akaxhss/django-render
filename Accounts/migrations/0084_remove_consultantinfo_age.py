# Generated by Django 3.2.4 on 2021-11-02 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0083_rename_is_otp_verified_user_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultantinfo',
            name='age',
        ),
    ]