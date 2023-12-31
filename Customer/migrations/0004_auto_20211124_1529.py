# Generated by Django 3.2.4 on 2021-11-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_medical'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='antenatalChart',
            field=models.FileField(blank=True, null=True, upload_to='antenatal'),
        ),
        migrations.AlterField(
            model_name='medical',
            name='bloodReport',
            field=models.FileField(blank=True, null=True, upload_to='bloodreport'),
        ),
        migrations.AlterField(
            model_name='medical',
            name='ultraSound',
            field=models.FileField(blank=True, null=True, upload_to='ultrasound'),
        ),
    ]
