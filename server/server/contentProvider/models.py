from django.db import models

# Create your models here.

class MovieToGuess(models.Model):
    userId = models.IntegerField()
    
    movie = models.FileField(upload_to = 'movies')
    ending = models.FileField(upload_to = 'movies')

    guessA = models.CharField(max_length=300)
    guessB = models.CharField(max_length=300)
