# Generated by Django 4.2.2 on 2023-11-06 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(default='blog/defualt.jpg', upload_to='blog'),
        ),
    ]
