from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):
    is_active = models.BooleanField(null=False, default=True)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='situations', null=True, blank=True)
    description = models.TextField(max_length=5000, null=False, blank=False)
    situation = models.ForeignKey(
        'locations.Situation', null=False, blank=False)
    user = models.ForeignKey(User)
    is_active = models.BooleanField(null=False, default=False)
    is_alive = models.BooleanField(null=False, default=True)
