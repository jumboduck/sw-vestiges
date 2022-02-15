from characters.models import Character
from .models import Location, Situation, LocationConnection
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json


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
                'characters': characters,
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


@staff_member_required
def locations_map(request):

    locations_json = {
        'nodes': [],
        'edges': [],
    }
    locations = Location.objects.all()
    for location in locations:
        if location.is_active:
            node = {
                'id': location.id,
                'label': location.name
            }
            locations_json['nodes'].append(node)
        else:
            continue

    location_connections = LocationConnection.objects.all()
    for connection in location_connections:
        if connection.is_active and connection.origin.is_active and connection.destination.is_active:
            edge = {
                "from": connection.origin.id,
                "to": connection.destination.id
            }
            locations_json['edges'].append(edge)
        else:
            continue

    context = {'locations_json': json.dumps(locations_json)}
    template = 'locations/location_map.html'
    return render(request, template, context)
