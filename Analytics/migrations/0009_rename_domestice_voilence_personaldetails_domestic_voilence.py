# Generated by Django 3.2.4 on 2022-02-25 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Analytics', '0008_alter_personaldetails_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personaldetails',
            old_name='domestice_voilence',
            new_name='domestic_voilence',
        ),
    ]
