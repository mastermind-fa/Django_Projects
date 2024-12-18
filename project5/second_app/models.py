from django.db import models

class myModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    check_field = models.BooleanField(default=False)
    date_field = models.DateField()
    datetime_field = models.DateTimeField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
    
