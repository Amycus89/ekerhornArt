from django.contrib import admin
from django.dispatch import receiver

# Register your models here.

from .models import Event
# Register your models here.
admin.site.register(Event)
