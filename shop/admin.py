from django.contrib import admin

from .models import Item, Purchase


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', ]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'item']
    search_fields = ['name', ]
