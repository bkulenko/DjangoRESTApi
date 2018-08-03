from django.db import models
from django.utils.dateparse import parse_date
import json

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
    DVD = models.DateField()
    BoxOffice = models.CharField(max_length=20)
    Production = models.CharField(max_length=50)
    Website = models.TextField()
    def set_ratings(self, rat):
        self.Ratings = json.loads(rat)

    def get_ratings(self):
        return json.dumps(self.Ratings)

    def set_released(self, date):
        self.Released = django.utils.dateformat.format(date, 'Y-m-d')
    
    def get_released(self):
        return django.utils.dateformat.format(self.Released, 'd M Y')

class Comment(models.Model):
    Movie = models.CharField(max_length=50)
    Comment = models.TextField()
