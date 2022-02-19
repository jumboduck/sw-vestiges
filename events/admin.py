from django.contrib import admin
from .models import Event, EventType


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_type',
        'situation_origin',
        'author',
        'created',
    )

    ordering = ('-created',)


class EventTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )

    ordering = ('name',)


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
