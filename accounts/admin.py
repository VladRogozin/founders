# accounts/admin.py
from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'coins', 'points', 'get_owned_skins')

    def get_owned_skins(self, obj):
        return ", ".join([skin.name for skin in obj.owned_skins.all()])

    get_owned_skins.short_description = 'Owned Skins'