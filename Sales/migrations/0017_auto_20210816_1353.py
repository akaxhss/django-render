# Generated by Django 3.2.4 on 2021-08-16 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0016_auto_20210816_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation',
            name='others_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='investigation',
            name='others_normal',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='investigation',
            name='others_value',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='investigation',
            name='tft_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='investigation',
            name='tft_normal',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='investigation',
            name='tft_value',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
