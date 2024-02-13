from .models import Painting
from django import forms
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
import environ

env = environ.Env()
environ.Env.read_env()

class PaintingForm(forms.Form):
    #Add autocomplete for name and email
    name = forms.CharField(label='Namn', label_suffix='', max_length=70, widget=forms.TextInput(attrs={'autocomplete': 'name'}))
    email = forms.EmailField(label='E-Mail', label_suffix='', widget=forms.TextInput(attrs={'autocomplete': 'email'}))
    message = forms.CharField(label='Meddelande', label_suffix='', widget=forms.Textarea, max_length=500)

# Create your views here.
def index(request):
    return render(request, "gallery/index.html", {
        "paintings": Painting.objects.all().order_by("-id")
    })

def painting(request, painting_id):
    if request.method == "POST": # If submit button was used
        # This will save all the user input of the form inside the variable "form":
        form = PaintingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            #Send email EMAIL_HOST
            # Subject should include the name of the painting
            subject = f"Ekerhorn Art - Från {name}, om \"{Painting.objects.get(id=painting_id).name}\""
            body = f"Från:\n{name}\n{email}\n\n{message}"
            recipient = f"Ekerhorn Art <{env('myEmail')}>"
            sender = f"{name} <{email}>"

            send_mail(subject, body, sender, [recipient], fail_silently=False) # Remove fail_silently once done testing
            # Redirect to painting, along with a success bool
            return HttpResponseRedirect(reverse('gallery:painting', args=(painting_id,)) + "?success=true")
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    # GET method
    painting = Painting.objects.get(id=painting_id)
    return render(request, "gallery/painting.html", {
        "painting": painting,
        "form": PaintingForm()
    })
