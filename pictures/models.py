from django.db import models
import datetime as dt

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
                return self.name

class Location(models.Model):
    city = models.CharField(max_length =30)
    country = models.TextField()

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/s')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =100)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
                return self.image_name
                
    def save_editor(self):
                self.save()

    @classmethod
    def get_image(cls,id):
        try:
                image=Image.objects.get(id=id)
                return image
        except DoesNotExist:

                return Image.objects.get(id=1)

    @classmethod
    def search_by_category(cls,search_term):
                category = Category.objects.filter(name__icontains=search_term).first()
                image = cls.objects.filter(category=category)
                return image

    class Meta:
                ordering = ['image_name']
