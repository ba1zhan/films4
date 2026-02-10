from django.contrib import admin
from moviess.models import Category, Movies, Fantasy
# Register your models here.

admin.site.register(Category)
admin.site.register(Fantasy)

@admin.register(Movies)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "created_at", "updated_at")
    list_filter = ("category",)