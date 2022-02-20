from django.contrib import admin
from .models import Character, PowerAttribute, ScienceAttribute, DexterityAttribute, \
    PersuasionAttribute, PoliticsAttribute, NavigationAttribute, PilotingAttribute, \
    RepairAttribute, DemolitionAttribute, PerceptionAttribute, ForceAttribute


class PowerAttrInline(admin.TabularInline):
    model = PowerAttribute


class ScienceAttrInline(admin.TabularInline):
    model = ScienceAttribute


class DexterityAttrInline(admin.TabularInline):
    model = DexterityAttribute


class PersuasionAttrInline(admin.TabularInline):
    model = PersuasionAttribute


class PoliticsAttrInline(admin.TabularInline):
    model = PoliticsAttribute


class NavigationAttrInline(admin.TabularInline):
    model = NavigationAttribute


class PilotingAttrInline(admin.TabularInline):
    model = PilotingAttribute


class RepairAttrInline(admin.TabularInline):
    model = RepairAttribute


class DemolitionAttrInline(admin.TabularInline):
    model = DemolitionAttribute


class PerceptionAttrInline(admin.TabularInline):
    model = PerceptionAttribute


class ForceAttrInline(admin.TabularInline):
    model = ForceAttribute


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'user',
        'situation',
        'is_active',
        'is_alive',
    )

    inlines = [PowerAttrInline, ScienceAttrInline, DexterityAttrInline, PersuasionAttrInline, PoliticsAttrInline,
               NavigationAttrInline, PilotingAttrInline, RepairAttrInline, DemolitionAttrInline, PerceptionAttrInline,
               ForceAttrInline]
    ordering = ('last_name', 'first_name',)


admin.site.register(Character, CharacterAdmin)
