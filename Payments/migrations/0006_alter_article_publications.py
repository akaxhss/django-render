# Generated by Django 3.2.4 on 2021-06-29 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0005_alter_article_publications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publications',
            field=models.ManyToManyField(related_name='related', to='Payments.Publication'),
        ),
    ]