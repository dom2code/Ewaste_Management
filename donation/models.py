from distutils.command.upload import upload
from unicodedata import name
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from yaml import add_implicit_resolver


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='images')
    category =  models.CharField(max_length=100, default='uncategorized')
    location =  models.CharField(max_length=100, default='undefined')
    # email=models.CharField(max_length=100, default='undefined')


    def __str__(self):
        return self.title + '|' + str(self.author)

    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# @property
# def get_photo_url(self):
#     if self.photo and hasattr(self.photo, 'url'):
#         return self.photo.url
#     else:
#         return "/media/ad_pics/ggg.png"