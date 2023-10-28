# Generated by Django 4.2.2 on 2023-07-05 15:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='created_data',
            new_name='updated_date',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='update_data',
        ),
        migrations.AddField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
