# Generated by Django 4.2.2 on 2023-11-07 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_post_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='about',
        ),
    ]