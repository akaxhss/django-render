# Generated by Django 3.2.4 on 2021-07-12 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0036_delete_lastupdatedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='consultant',
            field=models.BooleanField(default=False),
        ),
    ]
