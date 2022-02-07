from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product

# Create your views here.

def store(request, category_slug = None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug= category_slug )
        print(categories)
        products = Product.objects.filter(category = categories, is_available=True)
        products_count = products.count()
        
    else:
        products = Product.objects.all().filter(is_available= True)
        products_count = products.count()
    context = {
        'products':products,
        'count':products_count
    }
    return render(request, 'store/store.html',context)