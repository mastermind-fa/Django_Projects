from django.db import models
from musician.models import Musician

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title
