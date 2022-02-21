from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    @property
    def location(self):
        return self.situation.location


class Power(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    hand_to_hand = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    melee = models.PositiveIntegerField(null=True, blank=True, default=0)
    heavy_weapons = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    vigor = models.PositiveIntegerField(null=True, blank=True, default=0)


class Science(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    medicine = models.PositiveIntegerField(null=True, blank=True, default=0)
    bacta = models.PositiveIntegerField(null=True, blank=True, default=0)
    cybernetics = models.PositiveIntegerField(null=True, blank=True, default=0)
    survival = models.PositiveIntegerField(null=True, blank=True, default=0)
    xenobiology = models.PositiveIntegerField(null=True, blank=True, default=0)
    critical = models.PositiveIntegerField(null=True, blank=True, default=0)


class Dexterity(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    firing = models.PositiveIntegerField(null=True, blank=True, default=0)
    throwing = models.PositiveIntegerField(null=True, blank=True, default=0)
    jetpack = models.PositiveIntegerField(null=True, blank=True, default=0)
    dodge = models.PositiveIntegerField(null=True, blank=True, default=0)
    parade = models.PositiveIntegerField(null=True, blank=True, default=0)
    speed = models.PositiveIntegerField(null=True, blank=True, default=0)


class Persuasion(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    intimidation = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    command = models.PositiveIntegerField(null=True, blank=True, default=0)
    charisma = models.PositiveIntegerField(null=True, blank=True, default=0)
    seduction = models.PositiveIntegerField(null=True, blank=True, default=0)


class Politics(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    take_position = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    contest_position = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    start_rumor = models.PositiveIntegerField(null=True, blank=True, default=0)
    bribe = models.PositiveIntegerField(null=True, blank=True, default=0)
    poise = models.PositiveIntegerField(null=True, blank=True, default=0)
    scheming = models.PositiveIntegerField(null=True, blank=True, default=0)
    cultures = models.PositiveIntegerField(null=True, blank=True, default=0)
    promotion = models.PositiveIntegerField(null=True, blank=True, default=0)


class Navigation(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    shields = models.PositiveIntegerField(null=True, blank=True, default=0)
    artillery = models.PositiveIntegerField(null=True, blank=True, default=0)
    sensors = models.PositiveIntegerField(null=True, blank=True, default=0)
    astronavigation = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    astronomy = models.PositiveIntegerField(null=True, blank=True, default=0)


class Piloting(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    lasers = models.PositiveIntegerField(null=True, blank=True, default=0)
    missiles = models.PositiveIntegerField(null=True, blank=True, default=0)
    control = models.PositiveIntegerField(null=True, blank=True, default=0)
    dodge = models.PositiveIntegerField(null=True, blank=True, default=0)
    tactics = models.PositiveIntegerField(null=True, blank=True, default=0)
    adaptation = models.PositiveIntegerField(null=True, blank=True, default=0)


class Repair(models.Model):
    value = models.PositiveIntegerField(null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    ships = models.PositiveIntegerField(null=True, blank=True, default=0)
    droids = models.PositiveIntegerField(null=True, blank=True, default=0)
    comms = models.PositiveIntegerField(null=True, blank=True, default=0)
    system_d = models.PositiveIntegerField(null=True, blank=True, default=0)
    tactics = models.PositiveIntegerField(null=True, blank=True, default=0)
    jamming = models.PositiveIntegerField(null=True, blank=True, default=0)


class Demolition(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    traps = models.PositiveIntegerField(null=True, blank=True, default=0)
    explosives = models.PositiveIntegerField(null=True, blank=True, default=0)


class Perception(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    search = models.PositiveIntegerField(null=True, blank=True, default=0)
    clues = models.PositiveIntegerField(null=True, blank=True, default=0)
    hear_rumor = models.PositiveIntegerField(null=True, blank=True, default=0)
    detect_trap = models.PositiveIntegerField(null=True, blank=True, default=0)
    scouting = models.PositiveIntegerField(null=True, blank=True, default=0)


class Force(models.Model):
    value = models.PositiveIntegerField(null=True, blank=True, default=0)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    confusion = models.PositiveIntegerField(null=True, blank=True, default=0)
    compulsion = models.PositiveIntegerField(null=True, blank=True, default=0)
    telekenisis = models.PositiveIntegerField(null=True, blank=True, default=0)
    athleticism = models.PositiveIntegerField(null=True, blank=True, default=0)
    lightsaber = models.PositiveIntegerField(null=True, blank=True, default=0)
    focus = models.PositiveIntegerField(null=True, blank=True, default=0)
    psychic_protection = models.PositiveIntegerField(
        null=True, blank=True, default=0)


@receiver(post_save, sender=Character)
def create_attributes(sender, instance, created, **kwargs):
    if created:
        Power.objects.create(character=instance)
        Science.objects.create(character=instance)
        Dexterity.objects.create(character=instance)
        Persuasion.objects.create(character=instance)
        Politics.objects.create(character=instance)
        Navigation.objects.create(character=instance)
        Piloting.objects.create(character=instance)
        Repair.objects.create(character=instance)
        Demolition.objects.create(character=instance)
        Perception.objects.create(character=instance)
        Force.objects.create(character=instance)
