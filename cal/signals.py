from .models import EventDetails, Token, Calenders
from django.db.models.signals import post_save
from packages.calender_script import calendar_id_func
from django.dispatch import receiver


@receiver(post_save, sender=Token)
def create_calender(sender, instance, created, **kwargs):
    if instance and created:
        email = instance.email
        name = instance.name
        token_url = instance.token_file.url
        ids = calendar_id_func(name, token_url)
        print(ids)
        print('yes created!')
        for i in ids:
            print(i)
            Calenders.objects.create(name=f'{name}', ide=i[0], token_url=f'{token_url}', title = i[1])
        


