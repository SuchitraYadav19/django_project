from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    college = models.IntegerField(max_length=10)
    age = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)