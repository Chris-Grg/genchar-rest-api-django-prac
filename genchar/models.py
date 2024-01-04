from django.db import models

class GenshinChar(models.Model):
    name= models.CharField(max_length=200)
    stars=models.CharField(max_length=2)
    element=models.CharField(max_length=200)
    weapon=models.CharField(max_length=200)
    def __str__(self):
        return self.name