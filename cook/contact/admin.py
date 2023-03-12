from django.contrib import admin
from . import models


@admin.register(models.ContactModel)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "created_at"]
    list_display_links = ('name',)


admin.site.register(models.ContactLink)
admin.site.register(models.AboutModel)
