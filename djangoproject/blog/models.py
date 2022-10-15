from email.policy import default
from django.db import models
from account.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    date_created =  models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    read = models.IntegerField(default=0)
    image = models.ImageField(default='tech_blog_01.jpg', upload_to='post',  blank=True, null=True)

    def __str__(self):
        return self.title
