# Generated by Django 3.2.4 on 2022-08-22 07:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_criticalsymptoms_complication'),
    ]

    operations = [
        migrations.AddField(
            model_name='positivecriticalsymptoms',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
