# Generated by Django 3.2.4 on 2021-07-01 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0020_customerdetails_icmr'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordetails',
            name='icmr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='icmr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.doctordetails'),
        ),
    ]
