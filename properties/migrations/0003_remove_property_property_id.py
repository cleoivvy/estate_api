# Generated by Django 5.1.3 on 2024-11-28 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_remove_favorite_property_favorite_property_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='property_id',
        ),
    ]
