# Generated by Django 3.2.3 on 2022-02-20 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0008_auto_20220220_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='PowerAttr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('hand_to_hand', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('melee', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('heavy_weapons', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('vigor', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='attributes',
            name='power_oto',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.powerattr'),
        ),
    ]