from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    is_anim = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.user.username