# Generated by Django 3.2.3 on 2021-05-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='expires',
            field=models.DateField(null=True),
        ),
    ]
