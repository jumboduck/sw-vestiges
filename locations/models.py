from django.db import models


class Situation(models.Model):
    is_active = models.BooleanField(null=False, default=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='situations', null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    location = models.ForeignKey(
        'Location', null=False, blank=False, on_delete=models.CASCADE, default='void')
    display_rank = models.IntegerField(null=False, blank=False, default=0)


class Location(models.Model):
    is_active = models.BooleanField(null=False, default=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='locations', null=True, blank=True)
    description = models.TextField(max_length=2000, null=False, blank=False)
    display_rank = models.IntegerField(null=False, blank=False, default=0)


class LocationConnection(models.Model):
    is_active = models.BooleanField(null=False, default=True)
    origin = models.ForeignKey(
        'Location', null=False, blank=False, default='void')
    destination = models.ForeignKey(
        'Location', null=False, blank=False, default='void')
    is_reversible = models.BooleanField(null=False, blank=False, default=True)
