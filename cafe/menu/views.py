from wsgiref.simple_server import server_version

from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def menu_list(request):
    category_id=request.GET.get('category')

    products = Product.objects.all()
    search_query=request.GET.get('search')
    categories=Category.objects.all()

    if search_query:
        products = Product.objects.filter(name__icontains=search_query)

    if category_id:
        products=products.filter(category_id=category_id)

    context={
        'products':products,
        'categories':categories,
        'selected_category':category_id,
        'search_query':search_query
    }
    return render(request, 'menu/menu_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context={
        'product':product,
    }
    return render(request, 'menu/product_detail.html', context)