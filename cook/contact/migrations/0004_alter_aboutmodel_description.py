# Generated by Django 4.1.7 on 2023-03-07 15:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_aboutmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
    ]
