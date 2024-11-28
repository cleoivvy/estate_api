# Generated by Django 5.1.3 on 2024-11-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='property',
        ),
        migrations.AddField(
            model_name='favorite',
            name='property_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_id',
            field=models.IntegerField(default=1),
        ),
    ]