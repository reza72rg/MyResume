# Generated by Django 4.2.2 on 2023-11-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0032_remove_education_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='professionalexperience',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
