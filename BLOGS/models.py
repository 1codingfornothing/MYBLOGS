from django.db import models
"""导入User字段"""
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=99999)
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='blog', on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.CharField(max_length=200)
    blog = models.ForeignKey(Blog, related_name='comment', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)


