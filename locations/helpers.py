from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Situation, Location, LocationConnection
from profiles.models import UserProfile


def get_possible_destinations(origin_id):
    current_location = get_object_or_404(Situation, pk=origin_id)

    connections_to = LocationConnection.objects.filter(
        origin=current_location.location)

    connections_from = LocationConnection.objects.filter(
        destination=current_location.location,
        is_reversible=True)

    destinations = []

    for connection in connections_to:
        dest_situation = Situation.objects.filter(
            location=connection.destination).first()
        destinations.append(dest_situation)

    for connection in connections_from:
        dest_situation = Situation.objects.filter(
            location=connection.origin).first()
        destinations.append(dest_situation)

    return destinations


def get_current_location(request):
    profile = UserProfile.objects.get(user=request.user)
    return profile.active_character.situation.location
