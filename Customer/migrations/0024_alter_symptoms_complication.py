# Generated by Django 3.2.4 on 2022-02-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analytics', '0010_alter_customermedicalhistory_flag'),
        ('Customer', '0023_alter_symptoms_complication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptoms',
            name='complication',
            field=models.ManyToManyField(blank=True, to='Analytics.Complications'),
        ),
    ]