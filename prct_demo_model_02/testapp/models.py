from django.db import models

# Create your models here.
class EmpModel(models.Model):
    user=models.CharField(max_length=30)
    email=models.EmailField()

    def __str__(self):
        return 'user Name'+self.user
