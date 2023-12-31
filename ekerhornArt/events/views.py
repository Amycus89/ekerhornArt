from .models import Event
from django import forms
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
import environ

env = environ.Env()
environ.Env.read_env()

class ContactForm(forms.Form):
    #Add autocomplete for name and email
    name = forms.CharField(label='Namn', label_suffix='', max_length=70, widget=forms.TextInput(attrs={'autocomplete': 'name'}))
    email = forms.EmailField(label='E-Mail', label_suffix='', widget=forms.TextInput(attrs={'autocomplete': 'email'}))
    message = forms.CharField(label='Meddelande', label_suffix='', widget=forms.Textarea, max_length=500)

# Create your views here.
def index(request):
    return render(request, "events/index.html", {
        "events": Event.objects.all()
    })

def event(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, "events/event.html", {
        "event": event
    })
