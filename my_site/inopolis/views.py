from django.shortcuts import render


def index(request):
    return render(request, 'inopolis/index.html')


def film_page(request):
    return render(request, 'inopolis/film_page.html')
