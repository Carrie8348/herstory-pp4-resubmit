from django.shortcuts import (
    render, redirect, reverse, get_object_or_404,
    HttpResponseRedirect
)
from django.http import HttpResponseRedirect
from django.urls import reverse
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

    movie = get_object_or_404(Movie.objects.all(), pk=movie_id)
    reviews = Reviews.objects.filter(movie=movie)
    context = {
        'movie': movie,
        'reviews': reviews,
    }

    return render(request, 'movie/movie_detail.html', context)

def movie_likes(request, movie_id):
    """ A view to show how many likes the movie got """
    movie = get_object_or_404(Movie, id=request.POST.get('movie_id'))
    movie.likes.add(request.user)
    return HttpResponseRedirect(reverse('movie_detail', args=[str(movie_id)]))

