from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()

class Contact(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    area = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    email = models.EmailField(max_length=255, default='')
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
