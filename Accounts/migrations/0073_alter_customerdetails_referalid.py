# Generated by Django 3.2.4 on 2021-09-21 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0072_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='referalId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referal_doc', to='Accounts.doctordetails'),
        ),
    ]