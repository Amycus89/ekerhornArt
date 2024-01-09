from .models import Event
from django import forms
from django.shortcuts import render

import environ

env = environ.Env()
environ.Env.read_env()

# Create your views here.
def index(request):
    return render(request, "events/index.html", {
        #"paintings": Event.objects.all().order_by("-date")
    })

def painting(request, painting_id):
    painting = Painting.objects.get(id=painting_id)
    return render(request, "gallery/painting.html", {
        "painting": painting
    })
