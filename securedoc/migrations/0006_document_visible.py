# Generated by Django 3.2.8 on 2022-11-08 08:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('securedoc', '0005_remove_document_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='visible',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
