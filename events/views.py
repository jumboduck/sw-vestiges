from django.shortcuts import render, redirect, reverse
from django.contrib.admin.views.decorators import staff_member_required
from characters.forms import NewMessageForm
from characters.models import Character
from locations.helpers import get_characters_in_location
from events.models import Event, EventType


# @staff_member_required
# def create_animation_message(request, location):
#     if request.POST:
#         form = NewMessageForm(request.POST)
#         if form.is_valid():
#             recipients = form.cleaned_data['recipients']
#             if recipients == 'location':
#                 list_of_recipients = get_characters_in_location(location)
#             elif recipients == 'all':
#                 list_of_recipients = Character.objects.filter(active=True)
#             content = form.cleaned_data['content']

#             event = Event(
#                 author="Consulor",
#                 content=content,
#                 event_type=EventType.objects.get(name='Dialogue'),
#                 situation_origin=location.situation_set.filter(display_rank=1)
#             )
#             event.save()
#             event.recipients.set(list_of_recipients)
#             event.save()

#             return redirect(reverse('home'))
#     else:
#         form = NewMessageForm()

#         logs = Event.objects.filter(
#             recipients=active_character).order_by('-created')

#         context = {
#             'form': form,
#             'logs': logs,
#         }
#         template = 'characters/create_message.html'
#         return render(request, template, context)
