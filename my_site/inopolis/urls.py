from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='index'),
	path('about/<int:pk>', film_page, name='film_page'),
	path('about/random', random_film_page, name='random_film_page'),
    path('live-search', live_search, name='live-search'),
	path('/genre/<int:pk>/', show_genre, name='show_genre')
]