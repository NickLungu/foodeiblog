# Generated by Django 4.1.7 on 2023-03-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='number_of_likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
