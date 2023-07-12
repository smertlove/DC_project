from django.db import models

class Genre(models.Model):

    name = models.CharField()
    letter= models.CharField()



class Film(models.Model):

    title = models.CharField(max_length=64)
    genre = models.ManyToManyField("Genre")
    description = models.TextField()
    rating = models.CharField()
    director = models.CharField(max_length=64)
    producer = models.CharField(max_length=64)
    writer = models.CharField(max_length=64)
    release_date_theaters = models.DateField()
    release_date_streaming = models.DateField()


class Comment(models.Model):

    user = models.ForeignKey("User", on_delete=models.PROTECT)
    film = models.ForeignKey("Film", on_delete=models.PROTECT)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
