from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    movietitle=models.CharField(max_length=255)
    moviereleasedate=models.DateField()
    movieduration=models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True)
    moviedescription=models.TextField()
    movieurl=models.URLField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.movietitle
    
    class Meta:
        db_table='movie'
        verbose_name_plural='movies'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewrating=models.SmallIntegerField()
    reviewtext=models.TextField()
    
    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table='review'
        verbose_name_plural='reviews'

class Genre(models.Model):
    genre=models.CharField(max_length=255)
    genredescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.genre
    
    class Meta:
        db_table='genre'
        verbose_name_plural='genres'
