# Generated by Django 4.2.2 on 2023-11-07 14:25

from django.db import migrations, models
import mysite.tools


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_remove_post_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/defualt.jpg', upload_to=mysite.tools.UploadToPathAndRename('blog')),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(default='blog/defualt.jpg', upload_to=mysite.tools.UploadToPathAndRename('blog')),
        ),
    ]
