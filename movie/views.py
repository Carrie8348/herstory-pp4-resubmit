from django.shortcuts import (
    render, redirect, reverse, get_object_or_404,
    HttpResponseRedirect
)
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from review.models import Reviews
from .models import Movie


# Create your views here.
def MovieList(request):
    """ A view to show all products, including sorting and search queries """

    movies = Movie.objects.all()
    sort = None

    context = {
        'movies': movies,
    }

    return render(request, 'movie/index.html', context)

def movie_detail(request, movie_id):
    """ A view to show individual movie details """

    movie = get_object_or_404(Movie, pk=movie_id)
    #reviews = Reviews.objects.all()
    context = {
        'movie': movie,
        #"liked": liked,
        #"disliked": disliked,
        #'reviews': reviews,
    }

    return render(request, 'movie/movie_detail.html', context)

def movie_likes(request, movie_id):
    """ A view to show how many likes the movie got """
    movie = get_object_or_404(Movie, pk=movie_id)
    if movie.likes.filter(id=request.user.id).exists():
        movie.likes.remove(request.user)
    else:
        movie.likes.add(request.user)

