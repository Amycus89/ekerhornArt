from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from PIL import Image
import os
import shutil
from django.conf import settings
from django.core.validators import FileExtensionValidator

def process_name(painting_name):
    processed_name = painting_name.lower().replace(" ", "_").replace("ö", "o").replace("ä", "a").replace("å", "a").translate(str.maketrans("", "", "/:*?!#&\"<>|"))
    return processed_name

# Create your models here.

class Painting(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=46)
    painting = models.ImageField(upload_to="gallery/images", validators=[FileExtensionValidator(allowed_extensions=['jpg', 'webp', 'jpeg'])])
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
        # Add the meta image as well
        painting_image_urls['meta_url'] = f"{settings.MEDIA_URL}gallery/images/{painting_file_name}/{self.id}_{painting_file_name}_meta.jpg"
        return painting_image_urls



#Whenever admin adds new painting
@receiver(post_save, sender=Painting)
def resize_uploaded_image(sender, instance, created, **kwargs):
    if instance.painting:
        try:
            # Open the uploaded image
            img = Image.open(instance.painting)
            # Calculate aspect ratio
            aspect_ratio = img.width / img.height
            # Define the image widths
            image_widths = [20, 500, 960, 1800]
            # Define the painting file name
            painting_file_name = process_name(instance.name)
            for i, width in enumerate(image_widths):
                # Create a thumbnail with the specified width while maintaining the aspect ratio
                resized_img = img.copy()
                resized_img.resize((width, int(width / aspect_ratio)))
                #If there is no folder, create it
                if not os.path.exists(f"media/gallery/images/{painting_file_name}"):
                    os.makedirs(f"media/gallery/images/{painting_file_name}")
                # Save the resized images as jpgs
                resized_img.save(f"media/gallery/images/{painting_file_name}/{instance.id}_{painting_file_name}_{i}.jpg", quality=80, optimize=True)
                # Convert JPG to webp
                webp_img = resized_img.convert("RGB").convert("P", palette=Image.ADAPTIVE)
                # Save the webp images
                webp_img.save(f"media/gallery/images/{painting_file_name}/{instance.id}_{painting_file_name}_{i}.webp", optimize=True)

            # CREATE A META THUMBNAIL
            meta_width = 1200
            meta_height = 630
            # Check if the image dimensions are smaller than the target dimensions
            # Resize the image to have a width of 1200px while maintaining aspect ratio
            if img.width < meta_width:
                img = img.resize((meta_width, int(meta_width / aspect_ratio)))
            # Resize the image to have a height of 630px while maintaining aspect ratio
            if img.height < meta_height:
                img = img.resize((int(meta_height * aspect_ratio), meta_height))

            # Calculate the dimensions for cropping the resized image to the exact target size
            left = (img.width - meta_width) / 2
            top = (img.height - meta_height) / 2
            right = (img.width + meta_width) / 2
            bottom = (img.height + meta_height) / 2
            # Crop the resized image to the exact target size
            img = img.crop((left, top, right, bottom))
            # Save the thumbnail in the same folder
            img.save(f"media/gallery/images/{painting_file_name}/{instance.id}_{painting_file_name}_meta.jpg", quality=80, optimize=True)
            #Delete the old image
            os.remove(instance.painting.path)
        except FileNotFoundError:
            pass

@receiver(pre_delete, sender=Painting)
def delete_resized_images(sender, instance, **kwargs):
    # DELETE THE RESIZED IMAGES
    # Define the folder location
    folder_path = f"media/gallery/images/{process_name(instance.name)}/"
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
