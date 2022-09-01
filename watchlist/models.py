from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie


class Watchlist(models.Model):
    """
    Show watchlist for user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie,
                                      related_name='movie_watchlist')

    def __str__(self):
        return f'Watchlist ({self.user})'


class WatchListItem(models.Model):
    """
    Show watchlist items 
    """

    movie = models.ForeignKey(Movie,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    watchlist = models.ForeignKey(Watchlist,
                                 null=False,
                                 blank=False,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title