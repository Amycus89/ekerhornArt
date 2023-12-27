from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=46)
    background = models.ImageField(upload_to="images/")
    description = models.TextField()
    date = models.DateField()
    location_name = models.CharField(max_length=46)
    street = models.CharField(max_length=46)
    city = models.CharField(max_length=46)
    download_file = models.FileField(upload_to="files/", blank=True)
    read_more = models.URLField(blank=True)
