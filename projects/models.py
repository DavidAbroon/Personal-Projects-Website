from django.db import models
from PIL import Image

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='img/')

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path) # Open image using self

        if img.height > 1000 or img.width > 1000:
            new_img = (1000, 1000)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path


    def __str__(self):
        return self.title