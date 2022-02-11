from django.shortcuts import get_object_or_404, redirect, render
from carts.models import Cart, CartItem

from store.models import Product

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request)) #get the cart using cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    
    cart.save()
    
    #update  existing cart_item's quantity
    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    # create a new cartItem
    except CartItem.DoesNotExist:
        cart_item= CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart            
        )
        cart_item.save()
    #for the sake of checking
    # return HttpResponse(cart_item.product)
    # exit()
    
    return redirect('cart')
        
        
def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    # product = Product.objects.get(product_id = product_id)
    product = get_object_or_404(Product, id= product_id)
    cart_item = CartItem.objects.get(product = product, cart = cart)
    
    if cart_item.quantity > 1 :
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
        
    return redirect('cart')

def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    # product = Product.objects.get(product_id = product_id)
    product = get_object_or_404(Product, id= product_id)
    cart_item = CartItem.objects.get(product = product, cart = cart)
    cart_item.delete()
    
    return redirect('cart')
    

def cart(request):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart = cart, is_active=True)
        total = 0
        quantity =0
        for item in cart_items:
            total += (item.product.price * item.quantity)
            quantity += item.quantity
        tax = (8*total)/100
        grand_total = total-tax
    except Exception as e :
        pass
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax' : tax,
        'g_total': grand_total
    }
    return render(request,'store/cart.html',context)