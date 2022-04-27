from email.policy import default
from django.db import models
from django.forms import BooleanField

# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    completed= models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    student_age= models.IntegerField(default=False)

    def __str__(self) -> str:
        return self.first_name