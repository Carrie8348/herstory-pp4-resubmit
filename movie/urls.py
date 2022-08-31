from django.urls import path
from .import views

urlpatterns = [
    path('', views.MovieList, name='home'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    #path('like/', views.MovieLikes.as_view(), name='movie_like'),
    #path('dislike/', views.MovieDislikes.as_view(), name='movie_dislike'),
]