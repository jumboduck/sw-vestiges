from django.shortcuts import get_object_or_404
from .models import Situation, LocationConnection
from profiles.models import UserProfile
from characters.models import Character


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


def get_characters_in_situation(situation):
    return Character.objects.filter(situation=situation)


def get_characters_in_location(location):
    return Character.objects.filter(situation__location=location)
