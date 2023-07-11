from django.db import models
import requests
import schedule
import time

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=100, null=False, unique = True)
    text = models.CharField(max_length=5000, null=False)
    thumb = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200, null=False, default= ' ')
    company = models.CharField(max_length=200, null=False, default= ' ')


    

    def __repr__(self):
        return f"<[{self.title}]>"
