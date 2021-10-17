from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from characters.models import Character


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name="profile")
    active_character = models.ForeignKey(
        'characters.Character', null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    is_anim = models.BooleanField(null=False, blank=False, default=False)

    def set_active_character(self, character_id):
        new_active_character = get_object_or_404(Character, pk=character_id)
        if new_active_character.user == self:
            self.active_character = new_active_character
            self.save()
        else:
            return None

    def get_active_character(self):
        if self.active_character:
            return self.active_character
        else:
            return None

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return f'{self.user.username}, {self.active_character.id}'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.profile.save()
    instance.profile.save()
