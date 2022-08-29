from django.shortcuts import render
from django.views import generic
from .models import Movie

# Create your views here.
class MovieList(generic.ListView):
    model = Movie
    queryset = Movie.objects.filter(status=1).order_by('-updated_on')
    template_name = 'home.html'
    paginate_by = 4
