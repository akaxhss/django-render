# Generated by Django 3.2.4 on 2021-08-10 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0011_rename_rate_membershipplans_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='membership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Payments.membershipplans'),
        ),
    ]
