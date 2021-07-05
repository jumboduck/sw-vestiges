from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required

from .models import Location, Situation
from characters.models import Character


@login_required
def view_location(request, location_id):
    if request.user.is_superuser:
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
        return redirect(reverse('home'))
