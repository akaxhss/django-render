# Generated by Django 3.2.4 on 2022-08-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0103_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='SymptomsRemedy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(max_length=100)),
                ('remedy', models.TextField()),
            ],
        ),
    ]
