from django.contrib import admin

from phones.models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug']
    list_filter = ['name', 'price']
    prepopulated_fields = {"slug": ("name",)}
