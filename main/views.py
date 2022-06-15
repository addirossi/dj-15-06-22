from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Product


def index_page_view(request):
    text = 'Hello world!'
    return HttpResponse(text)


def products_list(request):
    a = 10000
    products = Product.objects.all()
    return render(request, 'main/oducts_list.html', context={'products': products})


def product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'main/product_details.html', {'product': product})
    except Product.DoesNotExist:
        raise Http404
