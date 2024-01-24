from .models import Painting
from django import forms
from django.shortcuts import render

import environ

env = environ.Env()
environ.Env.read_env()

# Create your views here.
def index(request):
    return render(request, "gallery/index.html", {
        "paintings": Painting.objects.all().order_by("-id")
    })

def painting(request, painting_id):
    painting = Painting.objects.get(id=painting_id)
    return render(request, "gallery/painting.html", {
        "painting": painting
    })
