from django.db import models
from django.utils import timezone


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name  # using the name of genre to be returned as a string / When added on admin page


class Console(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255)
    year_release = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)  # on delete means if genre or console
    console = models.ForeignKey(Console, on_delete=models.CASCADE)  # is deleted all games are also deleted
    date_created = models.DateTimeField(default=timezone.now)
