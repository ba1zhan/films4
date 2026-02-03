from django.shortcuts import render
from movies.models import Movies


# Movies.objects

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the movies index")


def movies_list(request):
    movies = Movies.objects.all()
    print(movies)
    return render(request, 'movies_list.html', context={'movies': movies})

def movies_detail(request, movies_id):
    movies = Movies.objects.get(id=movies_id)
    return render(request, "movies/movies_detail.html", context={"movies": movies})


def base(request):
    return render(request, "base.html")