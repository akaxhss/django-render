# Generated by Django 3.2.4 on 2023-07-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0108_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firebasefcm',
            name='fcm_token',
            field=models.TextField(blank=True, unique=True),
        ),
    ]
