
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Film, Comment, Genre
from django.http import JsonResponse
import random

def genre(request, films):
    genres = Genre.objects.all()
    request.COOKIES.setdefault("color_theme", "dark")
    return render(request, 'inopolis/index.html', {
        'films': films,
        'genres': genres,
        'gen': 0,
    })

def index(request):
    films = Film.objects.all()
    return genre(request, films)

def show_genre(request, pk):
    films = Film.objects.filter(genre=pk)
    return genre(request, films)


def add_comment(request, pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        content = request.POST.get('content')
        comment = Comment(content=content, film_id=pk, user_id=request.user.id)
        comment.save()
        return redirect('film_page', pk=pk)


def random_film_page(request):
    last_id = Film.objects.last().id
    random_id = random.randint(1, last_id)
    if request.method == 'POST':
        return add_comment(request, random_id)
    else:
        film = Film.objects.get(id = random_id)
        genre = film.genre.get()
        comments = Comment.objects.all().filter(film_id=random_id)
        comment_form = CommentForm()
        return render(request, 'inopolis/film_page.html', {
            'film': film,
            'genre': genre,
            'comments': comments,
            'comment_form': comment_form,
        })


def film_page(request, pk):
    if request.method == 'POST':
        return add_comment(request, pk)
    else:
        film = Film.objects.get(id=pk)
        comments = Comment.objects.all().filter(film_id=pk)
        comment_form = CommentForm()
        return render(request, 'inopolis/film_page.html', {
            'film': film,
            'comments': comments,
            'comment_form': comment_form,
        })






# ищет совпадения и возвращает список
def _live_search(pattern):
    matches = []
    if len(pattern)>0:
        matches = list(Film.objects.filter(title__istartswith=pattern))
    return [
        {"title": match.title}
        for match in matches
    ]


# вьюха
def live_search(request):
    print(1)

    pattern = request.GET.get('pattern')
    # if request.is_ajax():

    results = []
    if len(pattern) > 0:
        results = _live_search(pattern)
    return JsonResponse({'data': results})

    # я без понятия, что это означало
    # else:
    #     return entry(request)



