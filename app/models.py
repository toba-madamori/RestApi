from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogModel(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    email = models.EmailField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=False, related_name='blogs_id', blank=True, on_delete=models.CASCADE)

    


    def __str__(self):
        return self.title

