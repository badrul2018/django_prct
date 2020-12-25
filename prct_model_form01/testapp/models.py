from django.db import models

# Create your models here.
class StudModel(models.Model):
    name=models.CharField(max_length=30)
    roll=models.CharField(max_length=5)
    email=models.EmailField()
    gender=models.CharField(max_length=6)
    mark=models.FloatField()
    def __str__(self):
        return 'id'+self.roll

