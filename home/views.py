from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from characters.helpers import get_active_character
from locations.models import Situation, Location
from characters.models import Character


def index(request):
    template = 'home/index.html'
    if request.user.is_authenticated:
        active_character = get_active_character(request)
        if active_character:
            location_id = active_character.situation.location.id
            if active_character.is_active:
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
                }
                template = 'locations/location.html'

                return render(request, template, context)

            else:
                return render(request, 'home/awaiting_validation.html')
        else:
            return redirect(reverse('add_character'))

    """Display the home page"""
    return render(request, template)
