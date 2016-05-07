from django.contrib import admin

from . import models


# Register your models here.

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'zip_code')
    search_fields = ('city', 'zip_code')
    list_filter = ('state', )


@admin.register(models.TrustedIP)
class TrustedIP(admin.ModelAdmin):
    list_display = ('title', 'network', )
    search_fields = ('title', 'network')
