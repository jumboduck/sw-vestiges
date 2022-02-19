from django.shortcuts import get_object_or_404
from characters.models import Character
import random
import math


def activate_character(character_id):
    character = get_object_or_404(Character, pk=character_id)
    character.is_active = True
    character.save()


def deactivate_character(character_id):
    character = get_object_or_404(Character, pk=character_id)
    character.is_active = False
    character.save()


def dice_roll(stat):
    result = 0
    if stat == 0:
        return result
    dice = math.floor(stat / 3)
    remainder = stat % 3
    min = 1
    max = 6

    for _i in range(1, dice + 1):
        result += random.randint(min, max)

    return result + remainder
