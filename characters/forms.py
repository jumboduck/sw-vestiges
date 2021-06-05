from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    """
    # Create a new character
    """

    class Meta:
        model = Character
        fields = ['first_name', 'last_name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
