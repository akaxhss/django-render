# Generated by Django 3.2.4 on 2021-07-12 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0038_customerdetails_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordetails',
            name='experience',
            field=models.IntegerField(default=0),
        ),
    ]
