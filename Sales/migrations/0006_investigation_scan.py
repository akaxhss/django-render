# Generated by Django 3.2.4 on 2021-07-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0005_alter_custominvestigation_investigation'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation',
            name='scan',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
