from django.shortcuts import render
from .models import Product, Category


def menu_list(request):
    products = Product.objects.all()
    return render(request, 'menu/menu_list.html', {'products': products})