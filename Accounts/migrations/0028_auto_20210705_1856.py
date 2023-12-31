# Generated by Django 3.2.4 on 2021-07-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0027_user_datejoined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='Idproof',
        ),
        migrations.RemoveField(
            model_name='customerdetails',
            name='prescription',
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='abortions',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='allergic_reaction',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='babies_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='diabetes',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='doctor_final_visit',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='gynacology',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='hereditory',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='husband',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='job',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='marriedSince',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='no_of_babies_pregnant_with',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='surgery',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='twins',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
