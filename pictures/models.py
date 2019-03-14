from django.db import models


# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    email = models.EmailField()
    category = models.ForeignKey(Editor)
    location = models.ForeignKey(Editor)
    phone_number = models.CharField(max_length = 10,blank =True)

def __str__(self):
        return self.image_name
        
def save_editor(self):
        self.save()

class Meta:
        ordering = ['image_name']

# class tags(models.Model):
#     name = models.CharField(max_length =30)

#     def __str__(self):
#         return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/')

@classmethod
def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

@classmethod
def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

@classmethod
    
def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

