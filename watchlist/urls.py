from django.urls import path
from . import views

urlpatterns = [
    path('', views.watchlist, name='watchlist'),
    path('add_to_watchlist/<movie_id>',views.add_to_watchlist,name='add_to_watchlist'),
    path('remove_from_watchlist/<movie_id>',views.remove_from_watchlist,name='remove_from_watchlist'),
]