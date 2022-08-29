from django.urls import path
from .import views

urlpatterns = [
    path('', views.MovieList, name='movies'),
    #path('movie_detail/', views.MovieDetail.as_view(), name='movie_detail'),
    #path('like/', views.MovieLikes.as_view(), name='movie_like'),
    #path('dislike/', views.MovieDislikes.as_view(), name='movie_dislike'),
]