# Generated by Django 3.2.4 on 2021-11-01 04:45

import Accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0078_alter_user_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[Accounts.validators.CheckNull, Accounts.validators.CheckIfAlpha]),
        ),
    ]
