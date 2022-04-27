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