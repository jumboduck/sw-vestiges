from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Situation, Location, LocationConnection
from profiles.models import UserProfile


def get_possible_destinations(origin_id):
    origin_situation = get_object_or_404(Situation, pk=origin_id)
    origin_location = origin_situation.location

    connections_to = LocationConnection.objects.filter(
        origin=origin_location)

    connections_from = LocationConnection.objects.filter(
        destination=origin_location,
        is_reversible=True)

    neighbor_situations = Situation.objects.filter(
        location=origin_location
    )

    destinations = []

    for connection in connections_to:
        dest_situation = Situation.objects.filter(
            location=connection.destination).first()
        destinations.append(dest_situation)

    for connection in connections_from:
        dest_situation = Situation.objects.filter(
            location=connection.origin).first()
        destinations.append(dest_situation)

    for connection in neighbor_situations:
        destinations.append(connection)

    return destinations


def get_current_location(request):
    profile = UserProfile.objects.get(user=request.user)
    return profile.active_character.situation.location


def get_current_situation(request):
    profile = UserProfile.objects.get(user=request.user)
    return profile.active_character.situation
