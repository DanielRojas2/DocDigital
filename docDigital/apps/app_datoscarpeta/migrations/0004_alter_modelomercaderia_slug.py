# Generated by Django 5.1.4 on 2025-01-03 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_datoscarpeta', '0003_alter_modelomercaderia_options_modelomercaderia_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelomercaderia',
            name='slug',
            field=models.SlugField(max_length=75, unique_for_date='creado'),
        ),
    ]
