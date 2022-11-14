# Generated by Django 3.2.8 on 2022-11-07 15:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('securedoc', '0002_document_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='visible',
            field=models.ManyToManyField(related_name='visible', to=settings.AUTH_USER_MODEL),
        ),
    ]
