from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    contact=models.CharField(max_length=15, null=True)
    subject=models.CharField(max_length=50)
    message=models.TextField()
