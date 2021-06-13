from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required

from .models import Character
from .forms import CharacterForm, EditCharacterForm
from .helpers import get_active_character, set_active_character
from profiles.models import UserProfile
from locations.models import Location, Situation
from locations.helpers import get_possible_destinations, get_current_location


@login_required
def add_character(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            new_character = form.save()
            profile = UserProfile.objects.get(user=request.user)
            new_character.user = profile
            new_character.save()
            active_character = get_active_character(request)
            if not active_character:
                set_active_character(request, new_character.id)
            return redirect(reverse('character_detail', args=[new_character.id]))

    form = CharacterForm
    context = {'form': form, }
    template = 'characters/add_character.html'

    return render(request, template, context)


@login_required
def edit_character(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    if request.POST:
        form = EditCharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect(reverse('character_detail', args=[character.id]))

    form = CharacterForm(instance=character)
    context = {
        'character': character,
        'form': form,
    }
    template = 'characters/edit_character.html'

    return render(request, template, context)


@login_required
def character_detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    context = {
        'character': character,
    }
    template = 'characters/character_detail.html'

    return render(request, template, context)


@login_required
def move_active_character(request, destination_id):
    destination = Situation.objects.get(pk=destination_id)
    active_character = get_active_character(request)
    if active_character:
        active_character.situation = destination
        active_character.save()

        location = Location.objects.get(pk=destination.location.id)
        return redirect(reverse('view_location', args=[location.id]))

    return redirect(reverse('home'))


@login_required
def change_active_character_location(request):
    current_location = get_current_location(request)
    destinations = get_possible_destinations(current_location.id)
    context = {
        'destinations': destinations,
    }
    template = 'characters/change_location.html'
    return render(request, template, context)


@login_required
def user_character(request):
    profile = UserProfile.objects.get(user=request.user)
    characters = Character.objects.filter(user=profile)
    active_character = get_active_character(request)
    context = {
        'active_character': active_character,
        'characters': characters,
    }
    template = 'characters/list_user_characters.html'
    return render(request, template, context)


@login_required
def change_active_character(request, character_id):
    set_active_character(request, character_id)
    return redirect(reverse('home'))
