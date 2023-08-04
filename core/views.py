from django.shortcuts import render

from store.models import Product

def homepage(request):
    products = Product.objects.filter(status=Product.ACTIVE)
    context = {'products': products}
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')