# Generated by Django 3.2.3 on 2022-02-20 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0010_auto_20220220_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='PowerAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_value', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('hand_to_hand', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('melee', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('heavy_weapons', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('vigor', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('character', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
        migrations.CreateModel(
            name='ScienceAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_value', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('medicine', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('bacta', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('cybernetics', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('survival', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('xenobiology', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('critical', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('character', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
        migrations.RemoveField(
            model_name='powerattr',
            name='attributes',
        ),
        migrations.DeleteModel(
            name='Attributes',
        ),
        migrations.DeleteModel(
            name='PowerAttr',
        ),
    ]
