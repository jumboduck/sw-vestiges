# Generated by Django 3.2.3 on 2022-02-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_eventtype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtype',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]