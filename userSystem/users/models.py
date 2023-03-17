from pyexpat import model
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20, verbose_name='user Name')
    fullName = models.CharField(max_length=50, verbose_name='full Name')
    
    def __str__(self):
        userDetail = "usr: " + self.userName + " - " + " Full name : " + self.fullName 
        return userDetail
    
    
