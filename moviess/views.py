from django.shortcuts import redirect, render
from moviess.models import Movies, Category


# Movies.objects

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the movies index")


def movies_list(request):
    if request.method == "GET":
        movies = Movies.objects.all()
        categories = Category.objects.all()
        category_id = request.GET.get("category")
        search = request.GET.get("search")
        
        if category_id:
            movies = movies.filter(category_id=category_id)
        if search:
            movies = movies.filter(name__icontains=search)
            
        return render(
            request, 'movies/movies_list.html', context={'movies': movies, 'categories': categories, 'selected_category': category_id, 'search': search}
            )

def movies_detail(request, movies_id):
    if request.method == "GET":
        movies = Movies.objects.get(id=movies_id)
        return render(
              request, "movies/movies_detail.html", context={"movies": movies}
                      )
def movies_create(request):
    if request.method == "GET":
        return render(request, "movies/movies_create.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        category_id = request.POST.get("category")
        category = Category.objects.get(id=category_id)
        movies = Movies.objects.create(
            name=name, price=price, description=description, category=category
        )
        return redirect('/movies/')   
        


def base(request):
    if request.method == "GET":
        categoires = Category.objects.all()
        return render(request, "base.html", context={'categories': categoires})