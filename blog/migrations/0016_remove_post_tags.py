# Generated by Django 4.2.2 on 2023-11-06 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]