from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie


# Create your views here.
def index(request):
    # SELECT * FROM movies_movie
    movies = Movie.objects.all()
    # # SELECT * FROM movies_movies WHERE release_year = 1984
    # movie = Movie.objects.filter(release_year=1984)
    # Movie.objects.get(id=1)
    # output = ', '.join([m.title for m in movies])
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)
