from django.db import models

# Create your models here.

class HashTag(models.Model):
    tag = models.CharField(max_length=40)

    def __str__(self):
        return self.tag

class MovieToGuess(models.Model):
    userId = models.IntegerField()
    
    name = models.CharField(max_length=100)
    minature = models.FileField(upload_to = 'minatures')
    
    movie = models.FileField(upload_to = 'movies')
    ending = models.FileField(upload_to = 'movies')

    guessA = models.CharField(max_length=300)
    guessB = models.CharField(max_length=300)

    hashtags = models.ManyToManyField(HashTag)
    
    def __str__(self):
        return self.name
