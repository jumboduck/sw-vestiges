from django.contrib import admin
from .models import Character, Power, Science, Dexterity, Persuasion, Politics, Navigation, Piloting, \
    Repair, Demolition, Perception, Force


class PowerAttrInline(admin.TabularInline):
    model = Power


class ScienceAttrInline(admin.TabularInline):
    model = Science


class DexterityAttrInline(admin.TabularInline):
    model = Dexterity


class PersuasionAttrInline(admin.TabularInline):
    model = Persuasion


class PoliticsAttrInline(admin.TabularInline):
    model = Politics


class NavigationAttrInline(admin.TabularInline):
    model = Navigation


class PilotingAttrInline(admin.TabularInline):
    model = Piloting


class RepairAttrInline(admin.TabularInline):
    model = Repair


class DemolitionAttrInline(admin.TabularInline):
    model = Demolition


class PerceptionAttrInline(admin.TabularInline):
    model = Perception


class ForceAttrInline(admin.TabularInline):
    model = Force


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
