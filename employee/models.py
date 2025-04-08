from django.db import models

# Create your models here.


class Employee(models.Model):

    name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    active = models.BooleanField(default=True)
    department = models.CharField(max_length=20)

