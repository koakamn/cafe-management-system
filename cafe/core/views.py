from django.shortcuts import render
from menu.models import Product

def index(request):
    featured_products = Product.objects.all()[:3]
    context = {'featured_products': featured_products}
    return render(request, 'core/index.html',context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

