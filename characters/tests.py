from django.test import TestCase
from django.shortcuts import reverse
from django.utils.crypto import get_random_string

from .models import Character
from .forms import CharacterForm, EditCharacterForm
from .helpers import get_active_character


class CharactersTest(TestCase):
    def create_character(self, first_name=get_random_string(20), last_name=get_random_string(20), description=get_random_string(100)):
        return Character.objects.create(first_name=first_name, last_name=last_name, description=description)

    def test_character_creation(self):
        character = self.create_character()
        self.assertTrue(isinstance(character, Character))
        self.assertEqual(character.__str__(),
                         f'{character.first_name} {character.last_name}')

    def test_character_detail_view(self):
        character = self.create_character()
        url = reverse('character_detail',
                      args=[character.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(character.first_name, response.content.decode())

    def test_character_form_is_valid(self):
        data = {
            'first_name': 'Kalls',
            'last_name': 'Noroy',
            'description': 'long descriptive string',
        }
        form = CharacterForm(data)
        self.assertTrue(form.is_valid())

    def test_character_form_is_invalid(self):
        data = {
            'first_name': '',
            'last_name': 'Noroy',
            'description': 'long descriptive string',
        }
        form = CharacterForm(data)
        self.assertFalse(form.is_valid())

    def test_edit_character_form_is_valid(self):
        data = {
            'description': 'blablblablablalba'
        }
        form = EditCharacterForm(data)
        self.assertTrue(form.is_valid())

    def test_edit_character_form_is_invalid(self):
        data = {
            'description': ''
        }
        form = EditCharacterForm(data)
        self.assertFalse(form.is_valid())
