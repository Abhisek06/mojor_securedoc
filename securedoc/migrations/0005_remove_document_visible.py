# Generated by Django 3.2.8 on 2022-11-08 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securedoc', '0004_alter_document_visible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='visible',
        ),
    ]
