from audioop import reverse
from django.db import models
from django.conf import settings

class Genre(models.Model):

    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name


class Film(models.Model):

    ratings = [
        ("G", "G"),
        ("PG", "PG"),
        ("PG-13", "PG-13"),
        ("R", "R"),
        ("NC-17", "NC-17")
    ]

    title = models.CharField(max_length=64)
    genre = models.ManyToManyField("Genre")
    description = models.TextField()
    rating = models.CharField(max_length=5, choices=ratings)
    director = models.CharField(max_length=64)
    producer = models.CharField(max_length=64)
    writer = models.CharField(max_length=64)
    release_date_theaters = models.DateField()
    release_date_streaming = models.DateField()
    picture = models.ImageField(null=True)
    data = models.ImageField()

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    film = models.ForeignKey(Film, on_delete=models.PROTECT)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user} on {self.film} ({self.datetime})"
