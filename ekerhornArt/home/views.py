from django.shortcuts import render

# Create your views here.
def index(request):
    # Return the index.html in ekerhornArt/home/templates/home/index.html
    return render(request, "home/index.html")
