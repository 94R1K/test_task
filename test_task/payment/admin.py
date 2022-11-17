from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    list_editable = ('name', 'description', 'price')
    empty_value_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
