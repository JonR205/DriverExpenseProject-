from typing import ContextManager
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.FloatField()
    date_driven = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return(self.title) 