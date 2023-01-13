# Generated by Django 3.2.11 on 2022-01-17 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='firstname'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='lastname'),
        ),
    ]