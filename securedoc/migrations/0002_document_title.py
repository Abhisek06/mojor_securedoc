# Generated by Django 3.2.8 on 2022-11-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securedoc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
