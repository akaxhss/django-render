# Generated by Django 3.2.4 on 2021-11-15 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0015_alter_subscriptions_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='orderId',
            new_name='sub_Id',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='membership',
        ),
    ]
