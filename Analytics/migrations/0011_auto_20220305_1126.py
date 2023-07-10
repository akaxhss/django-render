# Generated by Django 3.2.4 on 2022-03-05 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analytics', '0010_alter_customermedicalhistory_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetails',
            name='frequency_of_call',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='notes',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='domestic_voilence',
            field=models.BooleanField(default=False),
        ),
    ]
