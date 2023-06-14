from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
	path('', views.index, name='index'),   #blog-home
	path('about/', views.film_page, name='film_page'),   #blog-about
]