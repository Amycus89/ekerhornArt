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
    if request.headers.get('x-requested-with') == 'XMLHttpRequest': # If submit button was used
        # This will save all the user input of the form inside the variable "form":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            #Send email EMAIL_HOST
            subject = f"{name} har kontaktat dig ang Ekerhorn Art"
            body = f"Email: {email}\n\n{message}"
            recipient = f"Ekerhorn Art <{env('myEmail')}>"
            sender = f"{name} <{email}>"

            send_mail(subject, body, sender, [recipient], fail_silently=False) # Remove fail_silently once done testing

            return JsonResponse({
                "success": True,
                "name": name
                })
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    # GET method
    return render(request, "home/index.html", {
	"form": ContactForm()
})
