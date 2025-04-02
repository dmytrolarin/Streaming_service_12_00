from .views import render_all_films, add_to_favorite,render_favorite_films, delete_from_favorite
from django.urls import path

urlpatterns = [
    path('all_films/', render_all_films, name = 'all_films'),
    path("add_to_favorite/<int:film_id>", add_to_favorite, name = "add_to_favorite"),
    path('favorite_films/', render_favorite_films, name = 'favorite_films'),
    path('delete_from_favorite/<int:film_id>', delete_from_favorite, name = 'delete_from_favorite')
]