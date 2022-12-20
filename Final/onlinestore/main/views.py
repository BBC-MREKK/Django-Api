from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Категории', 'url_name': 'cats'},
    {'title': 'Aвторизация', 'url_name': 'login'}

]

def index(request):
    products = Product.objects.all()
    context = [
        {'menu': menu},
        {'products': products},
    ]
    return render(request, 'main/index.html', context=context)

def cats(request):
    return render(request, 'main/cats.html')

def login(request):
    return render(request, 'main/login.html')

def show_post(request, post_slug):
    post = get_object_or_404(Product, slug=post_slug)
    context = [
        {'menu': menu},
        {'post': post}
    ]
    return render(request, 'main/show_post.html', context=context)

