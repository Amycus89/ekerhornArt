from django.shortcuts import render

from .models import Event

# Create your views here.
def index(request):
    return render(request, "events/index.html", {
        "events": Event.objects.all()
    })
