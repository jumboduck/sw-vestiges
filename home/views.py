from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from characters.helpers import get_active_character


def index(request):
    if request.user.is_authenticated:
        active_character = get_active_character(request)
        if active_character:
            if active_character.is_active:
                return redirect(reverse('view_location', args=[active_character.situation.location.id]))
            else:
                return render(request, 'home/awaiting_validation.html')
        else:
            return redirect(reverse('add_character'))

    """Display the home page"""
    return render(request, 'home/index.html')
