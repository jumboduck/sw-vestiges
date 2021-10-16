from django.shortcuts import get_object_or_404
from characters.models import Character


def activate_character(character_id):
    character = get_object_or_404(Character, pk=character_id)
    character.is_active = True
    character.save()


def deactivate_character(character_id):
    character = get_object_or_404(Character, pk=character_id)
    character.is_active = False
    character.save()
