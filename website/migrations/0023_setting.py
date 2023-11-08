# Generated by Django 4.2.2 on 2023-11-08 16:16

import ckeditor.fields
from django.db import migrations, models
import mysite.tools


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_alter_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create date')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='modify date')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='title')),
                ('site_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='site title')),
                ('site_icon', models.ImageField(upload_to=mysite.tools.UploadToPathAndRename('setting'), verbose_name='site icon')),
                ('site_logo', models.ImageField(upload_to=mysite.tools.UploadToPathAndRename('setting'), verbose_name='site logo')),
                ('contact_us', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'settings',
                'verbose_name_plural': 'settings',
            },
        ),
    ]
