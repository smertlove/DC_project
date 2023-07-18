from django.urls import path
from . import views
from inopolis import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/<int:pk>', views.film_page, name='film_page'),
	path('about/random', views.random_film_page, name='random_film_page')
]