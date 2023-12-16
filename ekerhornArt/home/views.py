from django import forms
from django.shortcuts import render
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(label='Namn', label_suffix='', max_length=70)
    email = forms.EmailField(label='E-Mail', label_suffix='')
    message = forms.CharField(label='Meddelande', label_suffix='', widget=forms.Textarea, max_length=500)

# Create your views here.
def index(request):
    if request.method == "POST": # If submit button was used
        # This will save all the user input of the form inside the variable "form":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            print(name, email, message)

            #Send email
            subject = f"{name} har kontaktat dig ang Ekerhorn Art"
            body = f"Email: {email}\n\n{message}"
            sender = "Ekerhorn Art <your@gmail.com>"
            recipient = f"{name} <{email}>"
            send_mail(subject, body, sender, [recipient], fail_silently=False) # Remove fail_silently once done testing
        else:
            render(request, "home/index.html", {
			"form": form # Will still show previously entered info, alongside error messages
		})

    # GET method
    return render(request, "home/index.html", {
	"form": ContactForm()
})
