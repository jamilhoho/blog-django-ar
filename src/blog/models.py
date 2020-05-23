from django.db import models
from django.contrib.auth.models import  User

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    post_date=models.DateTimeField(auto_now_add=True)
    post_update=models.DateTimeField(auto_now_add=True)
    auther=models.ForeignKey(User,on_delete=models.CASCADE)