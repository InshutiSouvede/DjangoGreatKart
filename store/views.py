from tokenize import single_quoted
from django import views
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from carts.models import Cart, CartItem
from carts.views import _cart_id

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

def product_detail(request,category_slug,product_slug):
    try:
        #get object->category->slug syntax use __
        single_product = Product.objects.get(category__slug = category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product = single_product).exists()
        
        #testing results
        # return HttpResponse(in_cart)
        # exit()
    except Exception as e:
        return e
    
    context = {
        'single_product':single_product, 
        'in_cart':in_cart
    }
        
    return render(request,'store/product_detail.html',context)