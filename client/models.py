from django.db import models


# Create your models here.
class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    Title = models.CharField(max_length=120)
    Author = models.CharField(max_length=120)
    Publisher = models.CharField(max_length=120)
    Image = models.CharField(max_length=500)

    def __str__(self):
        return self.ISBN
