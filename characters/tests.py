from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.crypto import get_random_string

from .models import Character
from .forms import CharacterForm, EditCharacterForm


class CharactersTest(TestCase):
    # Initialize
    def create_character(self, first_name=get_random_string(20), last_name=get_random_string(20), description=get_random_string(100)):
        return Character.objects.create(first_name=first_name, last_name=last_name, description=description)

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'simon', 'simon@randomemail.com', 'password')
        self.client.login(username='simon', password='password')

    # Models tests
    def test_character_creation(self):
        character = self.create_character()
        self.assertTrue(isinstance(character, Character))
        self.assertEqual(character.__str__(),
                         f'{character.first_name} {character.last_name}')

    # View tests
    def test_character_detail_view(self):
        character = self.create_character()
        url = reverse('character_detail',
                      args=[character.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(character.first_name, response.content.decode())

    def test_load_add_character_page(self):
        url = reverse('add_character')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_new_character_from_page(self):
        first_name = get_random_string(20)
        last_name = get_random_string(20)
        description = get_random_string(100)
        url = reverse('add_character')
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'description': description,
        }
        self.client.post(url, data)
        character = Character.objects.get(description=description)

        self.assertEqual(character.first_name, first_name)
        self.assertEqual(character.last_name, last_name)
        self.assertEqual(character.description, description)

    def test_redirect_after_creating_character_from_page(self):
        first_name = get_random_string(20)
        last_name = get_random_string(20)
        description = get_random_string(100)
        url = reverse('add_character')
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'description': description,
        }
        response = self.client.post(url, data)
        character = Character.objects.get(description=description)
        url = reverse('character_detail', args=[character.id])
        self.assertRedirects(response, url)

    # Form tests
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
