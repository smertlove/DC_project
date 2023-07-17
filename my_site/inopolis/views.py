from django.shortcuts import render
from .models import Film
import random

def index(request):

    request.COOKIES.setdefault("color_theme", "dark")

    return render(request, 'inopolis/index.html')


def film_page(request):
    last_id = Film.objects.last().id
    random_id = random.randint(1, last_id)
    obj = Film.objects.get(id = random_id)
    genre = obj.genre.get()
    request.COOKIES.setdefault("color_theme", "dark")
    request.film = {
        'title': obj.title,
        'genre': genre,
        'description': obj.description,
        'rating': obj.rating,
        'director': obj.director,
        'producer': obj.producer,
        'writer': obj.writer,
        'release_date_theaters': obj.release_date_theaters,
        'release_date_streaming': obj.release_date_streaming,
        'data': obj.data
    }
    return render(request, 'inopolis/random_film_page.html')
