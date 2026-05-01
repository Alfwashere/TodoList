from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(blank=True)
    priority=models.CharField(max_length=10, default='low')
