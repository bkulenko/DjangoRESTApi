from django.db import models


class Movie(models.Model):
    Title = models.TextField()
    Year = models.IntegerField()
    Rated = models.TextField()
    Released = models.DateField()
    Runtime = models.TextField()
    Genre = models.TextField()
    Director = models.TextField()
    Writer = models.TextField()
    Actors = models.TextField()
    Plot = models.TextField()
    Language = models.TextField()
    Country = models.TextField()
    Awards = models.TextField()
    Poster = models.TextField()
    Ratings = models.CharField(max_length=300)
    Metascore = models.CharField(max_length=20)
    imdbRating = models.CharField(max_length=10)
    imdbVotes = models.CharField(max_length=15)
    imdbID = models.CharField(max_length=15)
    Type = models.CharField(max_length=15)
    DVD = models.CharField(max_length=20)
    BoxOffice = models.CharField(max_length=20)
    Production = models.CharField(max_length=50)
    Website = models.TextField()


class Comment(models.Model):
    Movie = models.CharField(max_length=50)
    Comment = models.TextField()
