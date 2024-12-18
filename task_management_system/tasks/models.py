from django.db import models
from categories.models import Category

class Task(models.Model):
    title = models.CharField(max_length=50)
    
    content = models.TextField()
    category = models.ManyToManyField(Category)
    
    
    def __str__(self):
        return self.title