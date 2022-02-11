from django.contrib import admin

from .models import Cart, CartItem

# Register your models  to be added to the db.

admin.site.register(Cart)
admin.site.register(CartItem)
