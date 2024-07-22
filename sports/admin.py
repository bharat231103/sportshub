from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(Sport)
admin.site.register(Messages)
admin.site.register(Event)
admin.site.register(EventParticipation)


