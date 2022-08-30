from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from .models import Movie
# Create your views here.
def MovieList(request):
    """ A view to show all products, including sorting and search queries """

    movies = Movie.objects.all()
    query = None
    sort = None

    context = {
        'movies': movies,
    }

    return render(request, 'movie/index.html', context)

def movie_detail(request, movie_id):
    """ A view to show individual movie details """

    movie = get_object_or_404(MovieList, pk=movie_id)
    #reviews = Reviews.objects.all()
    context = {
        'movie': movie,
        #'reviews': reviews,
    }



    return render(request, 'movie/movie_detail.html', context)
