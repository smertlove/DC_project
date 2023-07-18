from django.shortcuts import render
from .models import Film, Comment
from django.contrib import auth
import random

def index(request):
    all_films = Film.objects.all()
    request.COOKIES.setdefault("color_theme", "dark")
    return render(request, 'inopolis/index.html', {'films': all_films})


# @login_required
# @require_http_methods(["POST"])
# def add_comment(request, film_id):
#     film = Film.objects.get(id = film_id)
#     comment = Comment.objects.get(film_id = film_id)
#     comment.film = film
#     comment.user = auth.get_user(id = comment.user_id)
#     comment.save()
#     try:
#         comment.path.extend(Comment.objects.get(id=form.cleaned_data['parent_comment']).path)
#         comment.path.append(comment.id)
#     except ObjectDoesNotExist:
#         comment.path.append(comment.id)
#
#     comment.save()
#
#     return redirect(article.get_absolute_url())

def random_film_page(request):
    last_id = Film.objects.last().id
    random_id = random.randint(1, last_id)
    film = Film.objects.get(id = random_id)
    genre = film.genre.get()
    return render(request, 'inopolis/film_page.html', {
        'film': film,
        'genre': genre,
    })

def film_page(request, pk):
    film = Film.objects.get(id = pk)
    return render(request, 'inopolis/film_page.html', {'film': film})
