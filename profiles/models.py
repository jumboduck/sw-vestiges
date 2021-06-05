from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    active_character = models.ForeignKey(
        'characters.Character', null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    is_anim = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return f'{self.user.username}, {self.active_character.id}'
