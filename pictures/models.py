from django.db import models
import datetime as dt

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
                return self.name

class Location(models.Model):
    city = models.CharField(max_length =30)
    country = models.TextField()

    def save_(self):
                self.save()

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =100)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    location = models.ForeignKey('Location',on_delete=models.CASCADE,)

    def __str__(self):
                return self.image_name
                
    

    @classmethod
    def get_image(cls,id):
        try:
                image=Image.objects.get(id=id)
                return image
        except DoesNotExist:

                return Image.objects.get(id=1)

    @classmethod
    def search_by_category(cls,search_term):
                # category = Category.objects.filter(name__icontains=search_term).first()
                image = cls.objects.filter(category__name__icontains=search_term)
                return image

    class Meta:
                ordering = ['image_name']

    @classmethod
    def search_by_location(cls,search_term):
                image_location = Location.objects.filter(location__country__icontains=search_term).first()
                return image_location