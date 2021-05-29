from django.contrib import admin
from .models import Location, Situation, LocationConnection


class SituationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'is_active',
    )

    ordering = ('location', 'name',)


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_active',
    )

    ordering = ('name',)


class LocationConnectionAdmin(admin.ModelAdmin):
    list_display = (
        'origin',
        'destination',
        'is_active',
    )

    ordering = ('origin', 'destination')


admin.site.register(Situation, SituationAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(LocationConnection, LocationConnectionAdmin)
