from django.db import models

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.CharField(max_length =60)
    country = models.TextField()

def search_by_title(cls,search_term):
        pictures = cls.objects.filter(title__icontains=search_term)
        return pictures


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/s')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

def __str__(self):
        return self.image_name
        
def save_editor(self):
        self.save()

class Meta:
        ordering = ['image_name']

