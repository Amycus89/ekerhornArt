from django.db import models

# Create your models here.

class Painting(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=46)
    painting = models.ImageField(upload_to="gallery/images")
    poem = models.TextField()

    def __str__(self):
        return f"{self.name}"
