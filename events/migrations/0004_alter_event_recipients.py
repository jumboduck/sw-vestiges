# Generated by Django 3.2.3 on 2021-07-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_alter_character_is_active'),
        ('events', '0003_alter_event_recipients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='recipients',
            field=models.ManyToManyField(blank=True, related_name='recipients', to='characters.Character'),
        ),
    ]
