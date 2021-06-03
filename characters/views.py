from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from .models import Character
from .forms import CharacterForm


@login_required
def add_character(request):
    # Create a new character
    form = CharacterForm
    context = {'form': form, }
    template = 'templates/add_character.html'

    return render(request, template, context)
