# Generated by Django 3.2.4 on 2021-11-08 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0030_alter_investigation_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercallreposnses',
            name='date',
            field=models.DateField(),
        ),
    ]