# Generated by Django 3.2.4 on 2021-11-05 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0008_alter_appointments_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointments',
            unique_together=set(),
        ),
    ]
