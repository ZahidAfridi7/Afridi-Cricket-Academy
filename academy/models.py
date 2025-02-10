from django.db import models
from django.core.validators import MinLengthValidator


class Players(models.Model):
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    DOP = models.DateField()
    Role = models.CharField(max_length=100,default='bowler')
    contact = models.IntegerField(max_length=14)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.full_name} is {self.Role}"

    
    
