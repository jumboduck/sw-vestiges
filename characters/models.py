from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):
    is_active = models.BooleanField(null=False, blank=False, default=True)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='situations', null=True, blank=True)
    description = models.TextField(max_length=5000, null=False, blank=False)
    situation = models.ForeignKey(
        'locations.Situation', null=False, blank=False, on_delete=models.PROTECT)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.SET_NULL)
    is_absent = models.BooleanField(null=False, default=False)
    is_alive = models.BooleanField(null=False, default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
