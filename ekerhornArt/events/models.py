from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from PIL import Image
import os
import shutil
from django.conf import settings
from django.core.validators import FileExtensionValidator

def process_name(event_name):
    processed_name = event_name.lower().replace(" ", "_").replace("ö", "o").replace("ä", "a").replace("å", "a").translate(str.maketrans("", "", "/:*?!#&\"<>|"))
    return processed_name

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
        # Add the meta image as well
        image_urls['meta_url'] = f"{settings.MEDIA_URL}events/images/{event_file_name}/{self.id}_{event_file_name}_meta.jpg"
        return image_urls

#Whenever admin creates new event
@receiver(post_save, sender=Event)
def resize_uploaded_image(sender, instance, created, **kwargs):
    # Check whether the object is created or if the background has changed
    if instance.background:
        try:
            # Open the uploaded image
            img = Image.open(instance.background)

            # Calculate aspect ratio
            aspect_ratio = img.width / img.height

            # Define the image widths
            image_widths = [20, 500, 1200, 1800]

            # Define the event file name
            event_file_name = process_name(instance.name)

            for i, width in enumerate(image_widths):
                # Resize the image to different resolutions
                resized_img = img.resize((width, int(width / aspect_ratio)))
                # Save the resized images as jpgs
                if not os.path.exists(f"media/events/images/{event_file_name}"):
                    os.makedirs(f"media/events/images/{event_file_name}")
                resized_img.save(f"media/events/images/{event_file_name}/{instance.id}_{event_file_name}_{i}.jpg", quality=80, optimize=True)
                # Convert JPG to webp
                webp_img = resized_img.convert("RGB").convert("P", palette=Image.ADAPTIVE)
                # Save the webp images
                webp_img.save(f"media/events/images/{event_file_name}/{instance.id}_{event_file_name}_{i}.webp", optimize=True)

            # CREATE A META IMAGE
            # if width of img is less than 1200px:
            if img.width < 1200:
                # Resize the image to have a width of 1200px while maintaining aspect ratio
                img = img.resize((1200, int(1200 / aspect_ratio)))
            if img.height < 630:
                # Resize the image to have a height of 630px while maintaining aspect ratio
                img = img.resize((int(630 * aspect_ratio), 630))

            #Crop the image towards the center to only be 1200px wide and 630px high
            img = img.crop((img.width/2 - 600, img.height/2 - 315, img.width/2 + 600, img.height/2 + 315))

            # Save the cropped image in the same folder
            img.save(f"media/events/images/{event_file_name}/{instance.id}_{event_file_name}_meta.jpg", quality=80, optimize=True)

            #Delete the old image
            os.remove(instance.background.path)
        except FileNotFoundError:
            pass


@receiver(pre_delete, sender=Event)
def delete_resized_images(sender, instance, **kwargs):
    # Delete the resized images
    # Define the painting file name
    folder_path = f"media/events/images/{process_name(instance.name)}/"
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
