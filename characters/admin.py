from django.contrib import admin
from .models import Character


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'situation',
        'is_active',
        'is_alive',
    )

    ordering = ('last_name', 'first_name',)


admin.site.register(Character, CharacterAdmin)
