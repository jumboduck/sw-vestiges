from django.shortcuts import render, get_object_or_404

from .models import Location, Situation


def view_location(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    situations = Situation.objects.filter(location=location)

    context = {
        'location': location,
        'situations': situations,
    }
    template = 'locations/location.html'

    return render(request, template, context)
