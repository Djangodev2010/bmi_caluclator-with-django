from django.db import models

# Create your models here.

class UnderweightTip(models.Model):
    title = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=600)
    
    def __str__(self):
        return self.title
    
class OverweightTip(models.Model):
    title = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=600)
    
    def __str__(self):
        return self.title

class RandomPopUp(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title