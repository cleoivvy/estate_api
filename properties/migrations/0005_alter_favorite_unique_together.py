# Generated by Django 5.1.3 on 2024-11-28 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_remove_favorite_property_id_favorite_created_at_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'property')},
        ),
    ]
