# Generated by Django 3.2.4 on 2021-06-29 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0004_auto_20210629_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publications',
            field=models.ManyToManyField(related_name='publication', to='Payments.Publication'),
        ),
    ]
