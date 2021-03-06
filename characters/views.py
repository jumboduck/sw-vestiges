from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Character
from .forms import CharacterForm, EditCharacterForm, NewMessageForm
from .helpers import dice_roll
from events.models import Event, EventType
from locations.models import Situation
from locations.helpers import get_possible_destinations, get_characters_in_situation, get_characters_in_location


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
    current_location = request.user.profile.active_character.situation
    possible_destinations = get_possible_destinations(current_location.id)
    chosen_destination = Situation.objects.get(pk=destination_id)
    active_character = request.user.profile.get_active_character()
    if active_character and chosen_destination in possible_destinations:
        if chosen_destination.location == current_location.location:
            destination_str = chosen_destination.name
        else:
            destination_str = chosen_destination.location
        event_content = f'{active_character} se d??place vers {destination_str}'
        event = Event(
            author=request.user.profile.get_active_character(),
            content=event_content,
            event_type=EventType.objects.get(name='Deplacement'),
            situation_origin=active_character.situation
        )
        event.save()
        origin_recipients = get_characters_in_location(
            current_location.location)
        destination_recipients = get_characters_in_location(
            chosen_destination.location)
        list_of_recipients = origin_recipients | destination_recipients
        event.recipients.set(list_of_recipients)
        event.save()
        active_character.situation = chosen_destination
        active_character.save()

        return redirect(reverse('home'))

    return redirect(reverse('home'))


@login_required
def view_active_character_destinations(request):
    active_character = request.user.profile.active_character
    current_location = active_character.situation
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
    active_character = request.user.profile.active_character
    if request.POST:
        form = NewMessageForm(request.POST)
        if form.is_valid():
            recipients = form.cleaned_data['recipients']
            if recipients == 'situation':
                list_of_recipients = get_characters_in_situation(
                    active_character.situation
                )
            elif recipients == 'location':
                list_of_recipients = get_characters_in_location(
                    active_character.location
                )
            content = form.cleaned_data['content']

            event = Event(
                author=request.user.profile.get_active_character(),
                content=content,
                event_type=EventType.objects.get(name='Dialogue'),
                situation_origin=active_character.situation
            )
            event.save()
            event.recipients.set(list_of_recipients)
            event.save()

            return redirect(reverse('home'))
    else:
        form = NewMessageForm()

        logs = Event.objects.filter(
            recipients=active_character).order_by('-created')

        context = {
            'form': form,
            'logs': logs,
        }
        template = 'characters/create_message.html'
        return render(request, template, context)


@login_required
def dexterity_test(request):
    difficulty = 4
    active_character = request.user.profile.active_character
    roll = dice_roll(active_character.dexterity.value)
    if roll >= difficulty:
        messages.add_message(request, messages.SUCCESS,
                             f'Jet de dext??rit?? {roll}/{difficulty}: r??ussi.')
    else:
        messages.add_message(request, messages.WARNING,
                             f'Jet de dext??rit?? {roll}/{difficulty}: ??chou??.')
    return redirect(reverse('home'))
