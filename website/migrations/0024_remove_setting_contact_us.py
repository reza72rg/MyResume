# Generated by Django 4.2.2 on 2023-11-08 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_setting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='contact_us',
        ),
    ]
