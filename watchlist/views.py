from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from movie.models import Movie
from .models import Watchlist


@login_required
def watchlist(request):
    """
    A view to render the user's watchlist
    """
    watchlist = None
    try:
        watchlist = Watchlist.objects.get(user=request.user)
    except Watchlist.DoesNotExist:
        pass

    context = {
        'watchlist': watchlist,
    }

    return render(request, 'watchlist/watchlist.html', context)


@login_required
def add_to_watchlist(request, movie_id):
    """
    For login-user to add item in the watchlist
    """
    movie = get_object_or_404(Movie, pk=movie_id)

    # Create a watchlist for the user if they don't have one
    watchlist, _ = Watchlist.objects.get_or_create(user=request.user)
    # Add product to the wishlist
    watchlist.movies.add(movie)
    messages.info(request, "A new movie was added to your watchlist")

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_watchlist(request, movie_id):
    """
    For login-user to remove item from the wishlist
    """
    watchlist = Watchlist.objects.get(user=request.user)
    movie = get_object_or_404(Movie, pk=movie_id)

    # Remove product from the wishlist
    watchlist.movies.remove(movie)
    messages.info(request, "A movie was removed from your wishlist")

    return redirect(request.META.get('HTTP_REFERER'))