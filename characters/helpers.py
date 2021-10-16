from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from characters.models import Character


def set_active_character(request, character_id):
    profile = UserProfile.objects.get(user=request.user)
    new_active_character = get_object_or_404(Character, pk=character_id)
    if new_active_character.user == profile:
        profile.active_character = new_active_character
        profile.save()
    else:
        return None


def activate_character(character_id):
    character = get_object_or_404(Character, pk=character_id)
    character.is_active = True
    character.save()


def deactivate_character(character_id):
    character = get_object_or_404(Character, pk=character_id)
    character.is_active = False
    character.save()
