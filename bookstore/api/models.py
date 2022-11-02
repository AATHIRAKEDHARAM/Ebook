import email
from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=10)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    class Meta:
        db_table="register"
