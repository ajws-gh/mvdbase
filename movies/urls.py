from django.urls import path
from .views import all_movies, AddMovie, EditMovie, DeleteMovie, DetailMovie, movie_reviews, DeleteReview

urlpatterns = [
    path('', all_movies, name='all_movies'),
    path('add_movie', AddMovie.as_view(), name='add_movie'),
    path('edit_movie/<int:pk>', EditMovie.as_view(), name='edit_movie'),
    path('delete_movie/<int:pk>', DeleteMovie.as_view(), name='delete_movie'),
    path('movie_details/<int:pk>', DetailMovie.as_view(), name='movie_details'),
    path('movie_reviews/<int:pk>', movie_reviews, name='movie_reviews'),
    path('delete_reviews/<int:pk>', DeleteReview.as_view(), name='delete_review'),
]