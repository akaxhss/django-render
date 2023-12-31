# Generated by Django 3.2.4 on 2021-06-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payments',
            name='status',
            field=models.IntegerField(choices=[(1, 'success'), (2, 'failed')], null=True),
        ),
    ]
