# Generated by Django 3.2.4 on 2021-06-18 08:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0014_rename_patientdetails_customerdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'.", regex='(0|91)?[7-9][0-9]{9}')]),
        ),
    ]
