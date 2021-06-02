from django.contrib import admin
from .models import Event, EventType, CharacterEvent


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'event_type',
        'situation_origin',
        'created',
    )

    ordering = ('-created')


class EventTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )

    ordering = ('name')


class CharacterEventAdmin(admin.ModelAdmin):
    list_display = (
        'character',
        'event',
    )

    ordering = ('character')


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(CharacterEvent, CharacterEventAdmin)
