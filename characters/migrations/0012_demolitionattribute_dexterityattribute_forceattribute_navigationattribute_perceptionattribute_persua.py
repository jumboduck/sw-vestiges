# Generated by Django 3.2.3 on 2022-02-20 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0011_auto_20220220_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_value', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('ships', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('droids', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('comms', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('system_d', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('tactics', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('jamming', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('character', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
        migrations.CreateModel(
            name='PoliticsAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_value', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('take_position', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('contest_position', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('start_rumor', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('bribe', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('poise', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('scheming', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('cultures', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('promotion', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('character', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
        migrations.CreateModel(
            name='PilotingAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_value', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('lasers', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('missiles', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('control', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('dodge', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('tactics', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('adaptation', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('character', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
        migrations.CreateModel(
            name='PersuasionAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_value', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('intimidation', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('command', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('charisma', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('seduction', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('character', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
        migrations.CreateModel(
            name='PerceptionAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_value', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('search', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('clues', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('hear_rumor', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('detect_trap', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('scouting', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('character', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
        migrations.CreateModel(
            name='NavigationAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_value', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('shields', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('artillery', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sensors', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('astronavigation', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('astronomy', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('character', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
        migrations.CreateModel(
            name='ForceAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_value', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('confusion', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('compulsion', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('telekenisis', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('athleticism', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('lightsaber', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('focus', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('psychic_protection', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('character', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
        migrations.CreateModel(
            name='DexterityAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_value', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('firing', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('throwing', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('jetpack', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('dodge', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('parade', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('speed', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('character', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
        migrations.CreateModel(
            name='DemolitionAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_value', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('traps', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('explosives', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('character', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
    ]
