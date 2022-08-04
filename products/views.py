from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /products -> index
def index(request):
  products = Product.objects.all()
  # return HttpResponse('Hello World')
  return render(request, 'index.html', {'products': products})


# /products/new -> new
def new(request):
  return HttpResponse('New Products')

