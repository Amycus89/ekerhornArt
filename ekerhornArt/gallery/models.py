from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
import os
from django.conf import settings

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

    def get_resized_image_urls(self):
        painting_file_name = process_name(self.name)
        painting_image_urls = {}
        for i in range(4):
            painting_image_urls[f'img_{i}_url'] = f"{settings.MEDIA_URL}gallery/images/{painting_file_name}/{self.id}_{painting_file_name}_{i}.jpg"
            # Add the webp images as well
            painting_image_urls[f'webp_{i}_url'] = f"{settings.MEDIA_URL}gallery/images/{painting_file_name}/{self.id}_{painting_file_name}_{i}.webp"
        return painting_image_urls



#Whenever admin adds new painting
@receiver(post_save, sender=Painting)
def resize_uploaded_image(sender, instance, created, **kwargs):
    # Check whether the object is created or if the painting has changed
    if not created and instance.painting != Event.objects.get(id=instance.id).painting:
        # Open the uploaded image
        img = Image.open(instance.painting)

        # Calculate aspect ratio
        aspect_ratio = img.width / img.height

        # Define the image widths
        image_widths = [20, 500, 960, 1800]

        for i, width in enumerate(image_widths):
            # Resize the image to different resolutions
            resized_img = img.resize((width, int(width / aspect_ratio)))
            # Define the painting file name
            painting_file_name = process_name(instance.name)
            # Save the resized images as jpgs
            if not os.path.exists(f"media/gallery/images/{painting_file_name}"):
                os.makedirs(f"media/gallery/images/{painting_file_name}")
            resized_img.save(f"media/gallery/images/{painting_file_name}/{instance.id}_{painting_file_name}_{i}.jpg", quality=80, optimize=True)
            # Convert JPG to webp
            webp_img = resized_img.convert("RGB").convert("P", palette=Image.ADAPTIVE)
            # Save the webp images
            webp_img.save(f"media/gallery/images/{painting_file_name}/{instance.id}_{painting_file_name}_{i}.webp", optimize=True)

        #Delete the old image
        os.remove(instance.painting.path)


def process_name(painting_name):
    processed_name = painting_name.lower().replace(" ", "_").replace("ö", "o").replace("ä", "a").replace("å", "a").translate(str.maketrans("", "", "/:*?!#&\"<>|"))
    return processed_name
