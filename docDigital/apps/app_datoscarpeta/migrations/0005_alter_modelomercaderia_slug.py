# Generated by Django 5.1.4 on 2025-01-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_datoscarpeta', '0004_alter_modelomercaderia_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelomercaderia',
            name='slug',
            field=models.SlugField(blank=True, max_length=75, null=True, unique_for_date='creado'),
        ),
    ]
