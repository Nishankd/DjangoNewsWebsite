from django.db import models
# Create your models here.


class Category(models.Model):
    # inherit gareko
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=500)

    def __str__(self):
        return self.name

