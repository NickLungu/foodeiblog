from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True)
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AboutModel(models.Model):
    name = models.CharField(max_length=100, default="")
    description = RichTextField()
