# Generated by Django 5.2.1 on 2025-06-11 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, null=True, verbose_name='phone'),
        ),
    ]
