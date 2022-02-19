from django.db import models


class Character(models.Model):
    is_active = models.BooleanField(null=False, blank=False, default=False)
    first_name = models.CharField(
        max_length=30, null=False, blank=False, verbose_name='prénom')
    last_name = models.CharField(
        max_length=30, null=False, blank=False, verbose_name='nom')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='characters', null=True, blank=True)
    description = models.TextField(max_length=5000, null=False, blank=False)
    situation = models.ForeignKey(
        'locations.Situation', null=True, blank=True, on_delete=models.PROTECT)
    user = models.ForeignKey('profiles.UserProfile', null=True, blank=True,
                             on_delete=models.SET_NULL)
    is_absent = models.BooleanField(null=False, blank=False, default=False)
    is_alive = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#     @property
#     def location(self):
#         return self.situation.location


class Attributes(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE,
                                     primary_key=True, null=False, blank=False)
    power = models.PositiveIntegerField(null=False, blank=False)
    science = models.PositiveIntegerField(null=False, blank=False)
    dexterity = models.PositiveIntegerField(null=False, blank=False)
    persuasion = models.PositiveIntegerField(null=False, blank=False)
    politics = models.PositiveIntegerField(null=False, blank=False)
    navigation = models.PositiveIntegerField(null=False, blank=False)
    repairs = models.PositiveIntegerField(null=False, blank=False)
    demolition = models.PositiveIntegerField(null=False, blank=False)
    perception = models.PositiveIntegerField(null=False, blank=False)
    force = models.PositiveIntegerField(null=False, blank=False)
