from django.urls import path
from .import views

urlpatterns = [
    path('', views.MovieList, name='home'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('like/<int:movie_id>', views.movie_likes, name='movie_likes'),
]