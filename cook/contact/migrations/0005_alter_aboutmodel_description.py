# Generated by Django 4.1.7 on 2023-03-07 16:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_aboutmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
