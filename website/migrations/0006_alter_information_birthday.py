# Generated by Django 4.2.2 on 2023-11-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='birthday',
            field=models.DateField(),
        ),
    ]
