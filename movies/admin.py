from django.contrib import admin
from movies.models import Category, Movies
# Register your models here.

admin.site.register(Category)

@admin.register(Movies)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "created_at", "updated_at")
    list_filter = ("category",)