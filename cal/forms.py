from django.forms import ModelForm
from cal.models import EventDetails

class CreateEventForm(ModelForm):
    class Meta:
        model = EventDetails
        fields = '__all__'
        

