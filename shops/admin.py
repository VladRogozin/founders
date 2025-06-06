from django.contrib import admin
from .models import AvatarItem

@admin.register(AvatarItem)
class AvatarItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price')
    search_fields = ('name',)