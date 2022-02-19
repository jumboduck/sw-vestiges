from django.contrib import admin
from .models import Character, Attributes


class AttributesInline(admin.TabularInline):
    model = Attributes


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'user',
        'situation',
        'is_active',
        'is_alive',
    )

    inlines = [AttributesInline, ]
    ordering = ('last_name', 'first_name',)


admin.site.register(Character, CharacterAdmin)
# admin.site.register(Attributes, AttributesInline)
