# Generated by Django 4.1.7 on 2023-03-07 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contactmodel_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]