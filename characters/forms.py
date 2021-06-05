from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ['first_name', 'last_name', 'description']


class EditCharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ['description']
