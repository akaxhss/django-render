# Generated by Django 3.2.4 on 2021-06-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0012_alter_doctordetails_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetails',
            name='interests',
            field=models.CharField(max_length=200, null=True),
        ),
    ]