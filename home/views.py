from django.shortcuts import render, redirect, reverse, get_object_or_404

from locations.models import Situation, Location
from characters.models import Character
from events.models import Event


def index(request):
    template = 'home/index.html'
    if request.user.is_authenticated:
        active_character = request.user.profile.get_active_character()
        if active_character:
            if active_character.is_active:
                location_id = active_character.situation.location.id
                logs = Event.objects.filter(
                    recipients=active_character).order_by('-created')
                location = get_object_or_404(Location, pk=location_id)
                situations = Situation.objects.filter(location=location)

                characters_situations = []

                for situation in situations:
                    characters = Character.objects.filter(situation=situation)
                    data = {
                        'situation': situation,
                        'characters': characters
                    }
                    characters_situations.append(data)

                context = {
                    'location': location,
                    'characters_situations': characters_situations,
                    'logs': logs,
                    "active_character": active_character,
                }
                template = 'locations/location.html'

                return render(request, template, context)

            else:
                return render(request, 'home/awaiting_validation.html')
        else:
            return redirect(reverse('add_character'))

    """Display the home page"""
    return render(request, template)
