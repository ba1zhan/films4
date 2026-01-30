from django.http import HttpResponse
from django.shortcuts import render

from films.models import Films

# select * from product;
# Product.objects.create()


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the product index.")


def Films_list(request):
    products = Films.objects.all()
    return render(request, "product_list.html", context={"products": products})