# Generated by Django 2.1.3 on 2018-11-09 13:26

import boards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=boards.models.get_image_path, verbose_name='image'),
        ),
    ]
