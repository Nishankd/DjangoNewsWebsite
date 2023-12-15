from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    date = models.DateField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slider = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    latest = models.BooleanField(default=False)
    slug = models.SlugField(max_length=500)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=50)
    def __str__(self):
        return self.address

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    subject = models.TextField(blank = True)
    message = models.TextField(blank = True)

    def __str__(self):
        return self.name