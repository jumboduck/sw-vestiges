# Generated by Django 3.2.3 on 2022-02-20 20:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0014_alter_power_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demolition',
            name='explosives',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='demolition',
            name='traps',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='demolition',
            name='value',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='dexterity',
            name='dodge',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='dexterity',
            name='firing',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='dexterity',
            name='jetpack',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='dexterity',
            name='parade',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='dexterity',
            name='speed',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='dexterity',
            name='throwing',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='dexterity',
            name='value',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='artillery',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='astronavigation',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='astronomy',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='sensors',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='shields',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='value',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='perception',
            name='clues',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='perception',
            name='detect_trap',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='perception',
            name='hear_rumor',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='perception',
            name='scouting',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='perception',
            name='search',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='perception',
            name='value',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='persuasion',
            name='charisma',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='persuasion',
            name='command',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='persuasion',
            name='intimidation',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='persuasion',
            name='seduction',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='persuasion',
            name='value',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='piloting',
            name='adaptation',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='piloting',
            name='control',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='piloting',
            name='dodge',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='piloting',
            name='lasers',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='piloting',
            name='missiles',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='piloting',
            name='tactics',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='piloting',
            name='value',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='politics',
            name='bribe',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='politics',
            name='contest_position',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='politics',
            name='cultures',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='politics',
            name='poise',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='politics',
            name='promotion',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='politics',
            name='scheming',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='politics',
            name='start_rumor',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='politics',
            name='take_position',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='politics',
            name='value',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='power',
            name='hand_to_hand',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='power',
            name='heavy_weapons',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='power',
            name='vigor',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='science',
            name='bacta',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='science',
            name='critical',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='science',
            name='cybernetics',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='science',
            name='medicine',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='science',
            name='survival',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='science',
            name='value',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='science',
            name='xenobiology',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(3)]),
        ),
    ]
