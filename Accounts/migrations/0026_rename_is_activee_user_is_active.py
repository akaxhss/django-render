# Generated by Django 3.2.4 on 2021-07-02 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0025_auto_20210702_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_activee',
            new_name='is_active',
        ),
    ]
