# Generated by Django 3.2.4 on 2021-11-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0080_alter_user_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetails',
            name='ProfilePic',
            field=models.FileField(blank=True, null=True, upload_to='ProfilePic/'),
        ),
    ]
