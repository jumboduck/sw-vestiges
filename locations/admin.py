from django.contrib import admin
from .models import Location, Situation, LocationConnection


class SituationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'is_active',
    )

    ordering = ('location', 'name',)


class SituationInline(admin.StackedInline):
    model = Situation
    extra = 0


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_active',
    )
    inlines = [SituationInline, ]

    ordering = ('name',)


class LocationConnectionAdmin(admin.ModelAdmin):
    list_display = (
        'origin',
        'destination',
        'is_active',
        'is_reversible',
    )

    ordering = ('origin', 'destination')


# admin.site.register(Situation, SituationAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(LocationConnection, LocationConnectionAdmin)
