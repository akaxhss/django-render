# Generated by Django 3.2.4 on 2021-08-16 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0064_auto_20210816_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='criticallity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.criticality'),
        ),
    ]
