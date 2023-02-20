from django.db import models
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


# Create your models here.
class Hashtag(models.Model):
    title = models.CharField(max_length=50)
    posts = models.ManyToManyField('Post', null=True, blank=True)

    def str(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    likes = models.IntegerField()
