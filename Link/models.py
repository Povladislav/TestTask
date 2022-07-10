from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    links = models.TextField(blank=True)

    def __str__(self):
        return self.author.username