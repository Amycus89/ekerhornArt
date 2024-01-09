from django.urls import path
from . import views # From current (.) directory, import views.py

app_name = "gallery"

urlpatterns = [
path("", views.index, name="index"),
path("<int:painting_id>/", views.gallery, name="gallery"),
]
