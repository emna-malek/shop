# Generated by Django 3.0.3 on 2020-04-26 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]