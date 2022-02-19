from django.db import models


class EventType(models.Model):
    is_active = models.BooleanField(null=False, blank=False, default=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='events', null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)

    @property
    def identifier(self):
        edited_name = ''.join(e for e in self.name if e.isalnum())
        return edited_name.lower()

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    is_active = models.BooleanField(null=False, blank=False, default=True)
    author = models.ForeignKey(
        'characters.Character', null=True, blank=True, on_delete=models.PROTECT, related_name='event_author'
    )
    recipients = models.ManyToManyField(
        'characters.Character', blank=True,
    )
    event_type = models.ForeignKey(
        EventType, null=False, blank=False, on_delete=models.PROTECT, default='')
    situation_origin = models.ForeignKey('locations.Situation', null=True, blank=True,
                                         on_delete=models.SET_NULL)
    created = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True, auto_now=True)
    content = models.TextField(max_length=4000, null=True, blank=True)

    @property
    def identifier(self):
        return self.event_type.identifier

    def __str__(self):
        message = ''
        date = self.created.strftime('%d/%m/%Y, %H:%M:%S')
        if self.author:
            message = f'({date}) {self.event_type} de {self.author}'
        else:
            message = f'({date}) {self.event_type}'
        return message
