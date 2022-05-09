from calendar import calendar
import imp
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import *  
from .models import  Token, EventDetails, Filter, Calenders


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.register(Calenders)
admin.site.register(Token)
admin.site.register(EventDetails)
admin.site.register(Filter)
