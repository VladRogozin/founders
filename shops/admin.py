from django.contrib import admin
from .models import AvatarItem, ComputerItem

@admin.register(AvatarItem)
class AvatarItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price')
    search_fields = ('name',)


@admin.register(ComputerItem)
class ComputerItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price')
    search_fields = ('name',)