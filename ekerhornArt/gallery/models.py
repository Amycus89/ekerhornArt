from django.db import models

# Create your models here.

class Painting(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=46)
    painting = models.ImageField(upload_to="gallery/images")
    poem = models.TextField()
    sold = models.BooleanField(default=False)
    width = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self):
        if self.sold:
            return f"{self.name} - SÅLD"
        else:
            return f"{self.name}"
