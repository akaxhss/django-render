# Generated by Django 3.2.4 on 2022-02-25 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analytics', '0005_medicalhistory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalhistory',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
