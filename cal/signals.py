from .models import EventDetails, Token, Calenders
from django.db.models.signals import post_save
from packages.calendar_ids import get_calendar_id
from django.dispatch import receiver


@receiver(post_save, sender=Token)
def create_calender(sender, instance, created, **kwargs):
    if instance and created:
        email = instance.email
        name = instance.name
        token_url = instance.token_file.url
        ids = get_calendar_id(name, token_url)
        for i in ids:
            Calenders.objects.create(name=f'{name}', ide=i[0], token_url=f'{token_url}', title = i[1])
        


