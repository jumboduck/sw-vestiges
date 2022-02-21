from django.contrib import admin
from django.forms.models import ModelForm
from .models import Character, Power, Science, Dexterity, Persuasion, Politics, Navigation, Piloting, \
    Repair, Demolition, Perception, Force


class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        """ Should returns True if data differs from initial. 
        By always returning true even unchanged inlines will get validated and saved."""
        return True


class PowerAttrInline(admin.TabularInline):
    model = Power
    extra = 1
    form = AlwaysChangedModelForm


class ScienceAttrInline(admin.TabularInline):
    model = Science
    extra = 1
    form = AlwaysChangedModelForm


class DexterityAttrInline(admin.TabularInline):
    model = Dexterity
    extra = 1
    form = AlwaysChangedModelForm


class PersuasionAttrInline(admin.TabularInline):
    model = Persuasion
    extra = 1
    form = AlwaysChangedModelForm


class PoliticsAttrInline(admin.TabularInline):
    model = Politics
    extra = 1
    form = AlwaysChangedModelForm


class NavigationAttrInline(admin.TabularInline):
    model = Navigation
    extra = 1
    form = AlwaysChangedModelForm


class PilotingAttrInline(admin.TabularInline):
    model = Piloting
    extra = 1
    form = AlwaysChangedModelForm


class RepairAttrInline(admin.TabularInline):
    model = Repair
    extra = 1
    form = AlwaysChangedModelForm


class DemolitionAttrInline(admin.TabularInline):
    model = Demolition
    extra = 1
    form = AlwaysChangedModelForm


class PerceptionAttrInline(admin.TabularInline):
    model = Perception
    extra = 1
    form = AlwaysChangedModelForm


class ForceAttrInline(admin.TabularInline):
    model = Force
    extra = 1
    form = AlwaysChangedModelForm


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
