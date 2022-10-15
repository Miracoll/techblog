from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(max_length=1000, blank=True, null=True)
    photo = models.ImageField(default='passport.jpg', upload_to='passport')
    gender = models.CharField(max_length=50, blank=True, null=True)