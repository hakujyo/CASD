from django.db import models
    
from django.utils import timezone


class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    number = models.IntegerField()