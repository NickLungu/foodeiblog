from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
# Register your models here.


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "create_date", "category", "title", "id"]
    inlines = [RecipeInline]
    save_as = True
    save_on_top = True


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "cook_time", "post", "id"]


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
