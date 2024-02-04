from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
import os
from django.conf import settings


# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=46)
    background = models.ImageField(upload_to="events/images")
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

    def get_resized_image_urls(self):
        event_file_name = process_name(self.name)
        img_0_url = f"{settings.MEDIA_URL}events/images/{self.id}_{event_file_name}_0.jpg"
        img_1_url = f"{settings.MEDIA_URL}events/images/{self.id}_{event_file_name}_1.jpg"
        img_2_url = f"{settings.MEDIA_URL}events/images/{self.id}_{event_file_name}_2.jpg"
        img_3_url = f"{settings.MEDIA_URL}events/images/{self.id}_{event_file_name}_3.jpg"
        return {
            'img_0_url': img_0_url,
            'img_1_url': img_1_url,
            'img_2_url': img_2_url,
            'img_3_url': img_3_url,
        }

#Whenever admin creates new event
@receiver(post_save, sender=Event)
def resize_uploaded_image(sender, instance, created, **kwargs):
    # Open the uploaded image
    img = Image.open(instance.background)

    # Calculate aspect ratio
    aspect_ratio = img.width / img.height
    img_0_Width = 20
    img_1_Width = 500
    img_2_Width = 1200
    img_3_Width = 1800

    # Resize the image to different resolutions
    img_0 = img.resize((img_0_Width, int(img_0_Width / aspect_ratio)))
    img_1 = img.resize((img_1_Width, int(img_1_Width / aspect_ratio)))
    img_2 = img.resize((img_2_Width, int(img_2_Width / aspect_ratio)))
    img_3 = img.resize((img_3_Width, int(img_3_Width / aspect_ratio)))

    # Save the resized images
    event_file_name = process_name(instance)
    img_0.save(f"media/events/images/{instance.id}_{event_file_name}_0.jpg", quality=80, optimize=True)
    img_1.save(f"media/events/images/{instance.id}_{event_file_name}_1.jpg", quality=80, optimize=True)
    img_2.save(f"media/events/images/{instance.id}_{event_file_name}_2.jpg", quality=80, optimize=True)
    img_3.save(f"media/events/images/{instance.id}_{event_file_name}_3.jpg", quality=80, optimize=True)

    #Convert to webp
    #webp_0 = img_0.convert("webp")
    #webp_0.save(f"media/events/images/{instance.id}_{event_file_name}_0.webp", quality=80, optimize=True)


    #Delete the old image
    os.remove(instance.background.path)


def process_name(event_name):
    processed_name = event_name.lower().replace(" ", "_").replace("ö", "o").replace("ä", "a").replace("å", "a").translate(str.maketrans("", "", "/:*?!#&\"<>|"))
    return processed_name
