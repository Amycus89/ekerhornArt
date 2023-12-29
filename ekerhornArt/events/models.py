import os
from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=46)
    background = models.ImageField(upload_to="events/images")
    description = models.TextField()
    date = models.DateField()
    location_name = models.CharField(max_length=46)
    street = models.CharField(max_length=46)
    city = models.CharField(max_length=46)
    download_file = models.FileField(upload_to="events/files", blank=True)
    read_more = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.date}"
