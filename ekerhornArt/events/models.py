from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
import os
from django.conf import settings
from django.core.validators import FileExtensionValidator


# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=46)
    background = models.ImageField(upload_to="events/images", validators=[FileExtensionValidator(allowed_extensions=['jpg', 'webp', 'jpeg'])])
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
        image_urls = {}
        for i in range(4):
            image_urls[f'img_{i}_url'] = f"{settings.MEDIA_URL}events/images/{event_file_name}/{self.id}_{event_file_name}_{i}.jpg"
            # Add the webp images as well
            image_urls[f'webp_{i}_url'] = f"{settings.MEDIA_URL}events/images/{event_file_name}/{self.id}_{event_file_name}_{i}.webp"
        return image_urls

#Whenever admin creates new event
@receiver(post_save, sender=Event)
def resize_uploaded_image(sender, instance, created, **kwargs):
    # Check whether the object is created or if the background has changed
    if not created and instance.background != Event.objects.get(id=instance.id).background:
        # Open the uploaded image
        img = Image.open(instance.background)

        # Calculate aspect ratio
        aspect_ratio = img.width / img.height

        # Define the image widths
        image_widths = [20, 500, 1200, 1800]

        for i, width in enumerate(image_widths):
            # Resize the image to different resolutions
            resized_img = img.resize((width, int(width / aspect_ratio)))
            # Define the event file name
            event_file_name = process_name(instance.name)
            # Save the resized images as jpgs
            if not os.path.exists(f"media/events/images/{event_file_name}"):
                os.makedirs(f"media/events/images/{event_file_name}")
            resized_img.save(f"media/events/images/{event_file_name}/{instance.id}_{event_file_name}_{i}.jpg", quality=80, optimize=True)
            # Convert JPG to webp
            webp_img = resized_img.convert("RGB").convert("P", palette=Image.ADAPTIVE)
            # Save the webp images
            webp_img.save(f"media/events/images/{event_file_name}/{instance.id}_{event_file_name}_{i}.webp", optimize=True)

        #Delete the old image
        os.remove(instance.background.path)


def process_name(event_name):
    processed_name = event_name.lower().replace(" ", "_").replace("ö", "o").replace("ä", "a").replace("å", "a").translate(str.maketrans("", "", "/:*?!#&\"<>|"))
    return processed_name
