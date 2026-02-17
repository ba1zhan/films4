from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from moviess.models import Movies, Category, Fantasy
from moviess.forms import MoviesForm, RegisterForm, LoginForm, SearchForm, CreateFilmForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, ListView


class MoviesListView(ListView):
    model = Movies
    template_name = "movies/movies_list.html"
    context_object_name = "movies"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["forms"] = SearchForm()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )
        category_id = self.request.GET.get("category_id")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        price_choice = self.request.GET.get("price_choice")
        if price_choice:
            if price_choice == "1":
                queryset = queryset.filter(price__gt=100)
            elif price_choice == "2":
                queryset = queryset.filter(price__lt=100)
        tags = self.request.GET.getlist("tags")
        if tags:
            queryset = queryset.filter(tags__in=tags)
        return queryset
    

class MoviesCreateView(CreateView):
    model = Movies
    template_name = "movies/movies_create.html"
    form_class = CreateFilmForm
    success_url = "/class/movies/"






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
    movies = Movies.objects.all()
    categories = Category.objects.all()
    tags = Fantasy.objects.all()
    
    selected_categories = request.GET.getlist("categories")
    if selected_categories:
        movies = movies.filter(category_id__in=selected_categories)
    
    selected_tags = request.GET.getlist("tags")
    if selected_tags:
        movies = movies.filter(tags__id__in=selected_tags).distinct()
    
    search = request.GET.get("search", "").strip()
    if search:
        movies = movies.filter(
            Q(name__icontains=search) | 
            Q(description__icontains=search)
        ).distinct()
    
    movies_qs = movies

    paginator = Paginator(movies_qs, 9)
    page_number = request.GET.get('page') or 1
    try:
        movies_page = paginator.page(page_number)
    except PageNotAnInteger:
        movies_page = paginator.page(1)
    except EmptyPage:
        movies_page = paginator.page(paginator.num_pages)

    params = request.GET.copy()
    if 'page' in params:
        params.pop('page')
    querystring = params.urlencode()

    context = {
        'movies': movies_page,
        'page_obj': movies_page,
        'paginator': paginator,
        'querystring': querystring,
        'total_movies': movies_qs.count(),
        'categories': categories,
        'tags': tags,
        'selected_categories': [int(c) for c in selected_categories],
        'selected_tags': [int(t) for t in selected_tags],
        'search': search,
    }
    return render(request, 'movies/movies_list.html', context)




def movies_detail(request, movies_id):
    movies = Movies.objects.get(id=movies_id)
    return render(request, "movies/movies_detail.html", context={"movies": movies})


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
    return render(request, "base.html")

def base(request):
    movies = Movies.objects.all()
    search = request.GET.get("search", "").strip()
    
    if search:
        movies = movies.filter(
            Q(name__icontains=search) | 
            Q(description__icontains=search)
        ).distinct()
    
    context = {
        'movies': movies,
        'search': search,
    }
    return render(request, "base.html", context)



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
    movies = Movies.objects.all()
    categories = Category.objects.all()
    tags = Fantasy.objects.all()
    
    selected_categories = request.GET.getlist("categories")
    if selected_categories:
        movies = movies.filter(category_id__in=selected_categories)
    
    selected_tags = request.GET.getlist("tags")
    if selected_tags:
        movies = movies.filter(tags__id__in=selected_tags).distinct()
    
    search = request.GET.get("search", "").strip()
    if search:
        movies = movies.filter(
            Q(name__icontains=search) | 
            Q(description__icontains=search)
        ).distinct()
    
    context = {
        'movies': movies,
        'categories': categories,
        'tags': tags,
        'selected_categories': [int(c) for c in selected_categories],
        'selected_tags': [int(t) for t in selected_tags],
        'search': search,
    }
    return render(request, 'movies/movies_list.html', context)




def movies_detail(request, movies_id):
    movies = Movies.objects.get(id=movies_id)
    return render(request, "movies/movies_detail.html", context={"movies": movies})


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
    return render(request, "base.html")

def base(request):
    movies = Movies.objects.all()
    search = request.GET.get("search", "").strip()
    
    if search:
        movies = movies.filter(
            Q(name__icontains=search) | 
            Q(description__icontains=search)
        ).distinct()
    
    context = {
        'movies': movies,
        'search': search,
    }
    return render(request, "base.html", context)