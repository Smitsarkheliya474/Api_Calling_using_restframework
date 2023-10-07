from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    salary = models.CharField(max_length=10)
    contact = models.CharField(max_length=20)
    address = models .CharField(max_length=20)