# Generated by Django 4.2.2 on 2023-11-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_skill_my_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='person',
        ),
        migrations.AddField(
            model_name='my_skill',
            name='percent',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
