from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from moviess.models import Movies, Category
from moviess.forms import MoviesForm, RegisterForm, LoginForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/movies/')
    else:
        form = RegisterForm()
    return render(request, "auth/register.html", {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/movies/')
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/movies/')


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
@login_required(login_url='/auth/login/')
def movies_create(request):
    if request.method == "GET":
        form = MoviesForm()
        return render(request, "movies/movies_create.html", context={'form': form})
    elif request.method == "POST":
        form = MoviesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/movies/')
        else:
            return render(request, "movies/movies_create.html", context={'form': form})   
        


def base(request):
    if request.method == "GET":
        movies = Movies.objects.all()
        return render(request, "base.html", context={'movies': movies})