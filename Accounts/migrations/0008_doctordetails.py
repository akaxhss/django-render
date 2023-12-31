# Generated by Django 3.2.4 on 2021-06-15 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_alter_patientdetails_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(max_length=200, null=True)),
                ('qualification', models.CharField(max_length=200, null=True)),
                ('medicalCouncil', models.CharField(max_length=20, null=True)),
                ('councilRegNo', models.CharField(max_length=200, null=True)),
                ('hospitals', models.CharField(max_length=300, null=True)),
                ('areaOfIntrerest', models.CharField(max_length=200, null=True)),
                ('placeOfWork', models.CharField(max_length=200, null=True)),
                ('onlineConsultation', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
