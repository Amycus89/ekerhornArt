from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
import os

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=46)
    background = models.ImageField(upload_to="")
    tags = models.CharField(max_length=46, blank=True)
    description = models.TextField()
    date = models.DateField()
    location_name = models.CharField(max_length=46)
    street = models.CharField(max_length=46)
    city = models.CharField(max_length=46)
    download_file = models.FileField(upload_to="events/files", blank=True)
    read_more = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.date}"

#Whenever admin creates new event
@receiver(post_save, sender=Event)
def resize_uploaded_image(sender, instance, created, **kwargs):
    # Open the uploaded image
    img = Image.open(instance.background)

    # Calculate aspect ratio
    aspect_ratio = img.width / img.height
    img_0_Width = 100
    img_1_Width = 273
    img_2_Width = 980
    img_3_Width = 1260

    # Resize the image to different resolutions
    img_0 = img.resize((img_0_Width, int(img_0_Width / aspect_ratio)))
    img_1 = img.resize((img_1_Width, int(img_1_Width / aspect_ratio)))
    img_2 = img.resize((img_2_Width, int(img_2_Width / aspect_ratio)))
    img_3 = img.resize((img_3_Width, int(img_3_Width / aspect_ratio)))

    # Save the resized images
    event_file_name = instance.name.replace(" ", "_").lower().translate(str.maketrans("", "", "/:*?!#&\"<>|"))
    print(event_file_name)
    img_0.save(f"media/events/images/{event_file_name}_p.jpg")
    img_1.save(f"media/events/images/{event_file_name}_s.jpg")
    img_2.save(f"media/events/images/{event_file_name}_m.jpg")
    img_3.save(f"media/events/images/{event_file_name}_l.jpg")

    # Delete the old image
    os.remove(instance.background.path)
    print("Image resized and saved")
