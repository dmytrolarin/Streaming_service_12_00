from django.db import models

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length= 255)
    description = models.TextField()
    preview_image = models.ImageField(upload_to = "images/film_previews")
    