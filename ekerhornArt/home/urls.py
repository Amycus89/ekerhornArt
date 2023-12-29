from django.urls import path
from . import views # From current (.) directory, import views.py

app_name = "home"

urlpatterns = [
path("", views.index, name="index"),
]
