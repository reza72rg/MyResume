# Generated by Django 4.2.6 on 2023-11-18 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0030_alter_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create date')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='modify date')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('title', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create date')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='modify date')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('title', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
