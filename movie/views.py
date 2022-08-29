from django.shortcuts import render
from .models import Movie

# Create your views here.
def MovieList(request):
    """ A view to show all products, including sorting and search queries """

    movies = Movie.objects.all()
    query = None
    sort = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                movies = movies.annotate(lower_name=Lower('name'))
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('movies'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            movies = movies.filter(queries)

    current_sorting = f'{sort}'

    context = {
        'movies': movies,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'movie/movies.html', context)
