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


class NewMessageForm(forms.Form):
    choices = (
        ('situation', 'Situation'),
        ('location', 'Lieu'),
    )
    recipients = forms.ChoiceField(
        label='Destinataires',
        choices=choices)
    content = forms.CharField(widget=forms.Textarea,
                              label='Message',
                              max_length=4000,
                              required=True)
