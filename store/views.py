from itertools import product
from django.shortcuts import render
from .models import Product

# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True)
    products_count = products.count()
    context = {
        'products':products,
        'count':products_count
    }
    return render(request, 'store/store.html',context)