from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    publication_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='icons/')
    desciption = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.user)
