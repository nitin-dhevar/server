from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    Title = models.CharField(max_length=120)
    Author = models.CharField(max_length=120)
    Publisher = models.CharField(max_length=120)
    Image = models.CharField(max_length=500)
    FA = models.IntegerField(default=0)
    Count = models.IntegerField(default=0)
    AC = models.IntegerField(default=0)
    desc = models.CharField(max_length=500,default="Sample Info About The Book working on it")
    pc = models.IntegerField(default=245)
    def __str__(self):
        return self.ISBN

class Bookissue(models.Model):
    Book = models.ForeignKey(Book,models.CASCADE)
    ACCNO = models.CharField(max_length=16)
    UID  = models.CharField(max_length=120,null=True)
    ED = models.DateTimeField(default=datetime.now()+timedelta(days=7))

class TokenData(models.Model):
    token = models.CharField(max_length=80)