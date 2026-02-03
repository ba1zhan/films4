from django.http import HttpResponse
from django.shortcuts import render
from movies.models import Movies


Movies.objects

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the movies index")


def movies_list(request):
    movies = Movies.objects.all()
    print(movies)
    return render(request, 'movies.html', context={'movies': movies})

def product_detail(request, product_id):
    product = Movies.objects.get(id=product_id)
    return render(request, "products/product_detail.html", context={"product": product})


def base(request):
    return render(request, "base.html")