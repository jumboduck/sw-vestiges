from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required

from .models import Character
from .forms import CharacterForm, EditCharacterForm, NewMessageForm
from events.models import Event, EventType
from locations.models import Situation
from locations.helpers import get_possible_destinations, get_current_situation, get_current_location, get_characters_in_situation, get_characters_in_location


@login_required
def add_character(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            new_character = form.save()
            profile = request.user.profile
            new_character.user = profile
            new_character.save()
            active_character = profile.get_active_character()
            if not active_character:
                request.user.profile.set_active_character(new_character.id)
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
    current_location = get_current_situation(request)
    possible_destinations = get_possible_destinations(current_location.id)
    chosen_destination = Situation.objects.get(pk=destination_id)
    active_character = request.user.profile.get_active_character()
    if active_character and chosen_destination in possible_destinations:
        active_character.situation = chosen_destination
        active_character.save()

        return redirect(reverse('home'))

    return redirect(reverse('home'))


@login_required
def view_active_character_destinations(request):
    current_location = get_current_situation(request)
    destinations = get_possible_destinations(current_location.id)

    neighbor_situations = filter(
        lambda destination: destination.location == current_location.location,
        destinations
    )

    other_location_situations = filter(
        lambda destination: destination.location != current_location.location,
        destinations
    )

    context = {
        'current_location': current_location,
        'destinations': destinations,
        'situations': neighbor_situations,
        'locations': other_location_situations,
    }
    template = 'characters/change_location.html'
    return render(request, template, context)


@login_required
def user_character(request):
    profile = request.user.profile
    characters = Character.objects.filter(user=profile)
    active_character = profile.get_active_character()
    context = {
        'active_character': active_character,
        'characters': characters,
    }
    template = 'characters/list_user_characters.html'
    return render(request, template, context)


@login_required
def change_active_character(request, character_id):
    request.user.profile.set_active_character(character_id)
    return redirect(reverse('home'))


@login_required
def create_message(request):
    if request.POST:
        form = NewMessageForm(request.POST)
        if form.is_valid():
            recipients = form.cleaned_data['recipients']
            if recipients == 'situation':
                list_of_recipients = get_characters_in_situation(
                    get_current_situation(request)
                )
            elif recipients == 'location':
                list_of_recipients = get_characters_in_location(
                    get_current_location(request)
                )
            content = form.cleaned_data['content']

            event = Event(
                author=request.user.profile.get_active_character(),
                content=content,
                event_type=EventType.objects.get(name='Dialogue'),
                situation_origin=get_current_situation(request)
            )
            event.save()
            event.recipients.set(list_of_recipients)
            event.save()

            return redirect(reverse('home'))
    else:
        form = NewMessageForm()
        context = {
            'form': form,
        }
        template = 'characters/create_message.html'
        return render(request, template, context)
