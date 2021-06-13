from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()
    instance.userprofile.save()
