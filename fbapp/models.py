from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AppModel(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default="No Description Given For this App")
    placeholder = models.CharField(max_length=40)
    randoms = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.URLField(default="https://i.imgur.com/5lH7xkG.jpg")
    def __str__(self): return self.name
    
    class Meta:
        ordering = ['-pk']


class Result(models.Model):
    imgurl = models.URLField()
    name = models.CharField(max_length=20)
    apppk = models.IntegerField()
    def __str__(self): self.name

