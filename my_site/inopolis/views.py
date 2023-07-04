from django.shortcuts import render


def index(request):

    request.COOKIES.setdefault("color_theme", "dark")

    return render(request, 'inopolis/index.html')


def film_page(request):

    request.COOKIES.setdefault("color_theme", "dark")

    return render(request, 'inopolis/film_page.html')
