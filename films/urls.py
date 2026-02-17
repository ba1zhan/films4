"""
URL configuration for films project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import static
from moviess.views import base, movies_detail, movies_list, movies_create, register, login_view, logout_view, MoviesListView, MoviesCreateView
from django.conf import settings


class_urls = [
    path("class/movies/", MoviesListView.as_view()),
    path("class/movies_create/", MoviesCreateView.as_view()),
]



user_urls = [
    path('auth/register/', register),
    path('auth/login/', login_view),
    path('auth/logout/', logout_view)
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),
    path('movies/', movies_list),
    path('movies/create/', movies_create),
    path("movies/<int:movies_id>/", movies_detail),
    *class_urls,
    *user_urls
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
