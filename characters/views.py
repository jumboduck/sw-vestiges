from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required

from .models import Character
from locations.models import Location, Situation
from .forms import CharacterForm, EditCharacterForm

from .helpers import get_active_character


@login_required
def add_character(request):
    # Create a new character
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save()
            return redirect(reverse('character_detail', args=[character.id]))

    form = CharacterForm
    context = {'form': form, }
    template = 'characters/add_character.html'

    return render(request, template, context)


@login_required
def edit_character(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    print("hi")

    if request.POST:
        print('inside post')
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
