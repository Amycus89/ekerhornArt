from .models import Event
from django import forms
from django.shortcuts import render

import environ

env = environ.Env()
environ.Env.read_env()

# Create your views here.
def index(request):
    return render(request, "events/index.html", {
        "events": Event.objects.all().order_by("-date")
    })

def event(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, "events/event.html", {
        "event": event
    })
