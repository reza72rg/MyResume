# Generated by Django 4.2.2 on 2023-11-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_remove_skill_person_my_skill_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='create date'),
        ),
        migrations.AddField(
            model_name='information',
            name='image',
            field=models.ImageField(default='website/defualt.jpg', upload_to='website/%y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='information',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='information',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='modify date'),
        ),
    ]
