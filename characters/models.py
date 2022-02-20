from django.db import models
from django.core.validators import MinValueValidator


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

    # @property
    # def power(self):
    #     return self.power.value

    # @property
    # def science(self):
    #     return self.science.value

    # @property
    # def xdexterity(self):
    #     return self.dexterity.value

    # @property
    # def persuasion(self):
    #     return self.persuasion.value

    # @property
    # def politics(self):
    #     return self.politics.value

    # @property
    # def navigation(self):
    #     return self.navigation.attr_value

    # @property
    # def piloting(self):
    #     return self.piloting.attr_value

    # @property
    # def repair(self):
    #     return self.repair.attr_value

    # @property
    # def demolition(self):
    #     return self.demolition.attr_value

    # @property
    # def perception(self):
    #     return self.perception.attr_value

    # @property
    # def force(self):
    #     return self.force.attr_value


class Power(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    hand_to_hand = models.PositiveIntegerField(validators=[MinValueValidator(3)],
                                               null=True, blank=True, default=3)
    melee = models.PositiveIntegerField(null=True, blank=True, default=3)
    heavy_weapons = models.PositiveIntegerField(validators=[MinValueValidator(3)],
                                                null=True, blank=True, default=3)
    vigor = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)


class Science(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    medicine = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    bacta = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    cybernetics = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    survival = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    xenobiology = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    critical = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)


class Dexterity(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    firing = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    throwing = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    jetpack = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    dodge = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    parade = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    speed = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)


class Persuasion(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    intimidation = models.PositiveIntegerField(validators=[MinValueValidator(3)],
                                               null=True, blank=True, default=3)
    command = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    charisma = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    seduction = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)


class Politics(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    take_position = models.PositiveIntegerField(validators=[MinValueValidator(3)],
                                                null=True, blank=True, default=3)
    contest_position = models.PositiveIntegerField(validators=[MinValueValidator(3)],
                                                   null=True, blank=True, default=3)
    start_rumor = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    bribe = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    poise = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    scheming = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    cultures = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    promotion = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)


class Navigation(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    shields = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    artillery = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    sensors = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    astronavigation = models.PositiveIntegerField(validators=[MinValueValidator(3)],
                                                  null=True, blank=True, default=3)
    astronomy = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)


class Piloting(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    lasers = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    missiles = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    control = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    dodge = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    tactics = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    adaptation = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)


class Repair(models.Model):
    value = models.PositiveIntegerField(null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    ships = models.PositiveIntegerField(null=True, blank=True, default=3)
    droids = models.PositiveIntegerField(null=True, blank=True, default=3)
    comms = models.PositiveIntegerField(null=True, blank=True, default=3)
    system_d = models.PositiveIntegerField(null=True, blank=True, default=3)
    tactics = models.PositiveIntegerField(null=True, blank=True, default=3)
    jamming = models.PositiveIntegerField(null=True, blank=True, default=3)


class Demolition(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    traps = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    explosives = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)


class Perception(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    character = models.OneToOneField(
        Character, null=True, on_delete=models.CASCADE)
    search = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    clues = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    hear_rumor = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    detect_trap = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)
    scouting = models.PositiveIntegerField(
        validators=[MinValueValidator(3)], null=True, blank=True, default=3)


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
