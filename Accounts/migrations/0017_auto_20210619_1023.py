# Generated by Django 3.2.4 on 2021-06-19 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0016_alter_user_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='Idproof',
            field=models.FileField(null=True, upload_to='Idproof/'),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='prescription',
            field=models.FileField(null=True, upload_to='Prescriptions/'),
        ),
    ]
