from django.urls import path
from . import views
from inopolis import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.film_page, name='film_page'),
]