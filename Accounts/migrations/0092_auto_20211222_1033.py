# Generated by Django 3.2.4 on 2021-12-22 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0091_alter_user_firstname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='profile_img',
        ),
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='ProfilePic/'),
        ),
    ]