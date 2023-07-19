from django.db import models

# Create your models here.
class Movie(models.Model):
    
    desc = models.CharField(max_length=10000)
    
    