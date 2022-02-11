
from django.urls import path

from carts import views 

urlpatterns = [
    path('',views.cart,name='cart'),
    path('add_cart/<int:product_id>/',views.add_cart, name='add_cart'),#since we need to pass product Id
    path('remove_cart/<int:product_id>/',views.remove_cart, name='remove_cart'),#since we need to pass product Id
    path('remove_cart_item/<int:product_id>/',views.remove_cart_item, name='remove_cart_item')#since we need to pass product Id
]
# urlpatterns = [
#     path('', views.store,name='store'),
#     path('<slug:category_slug>/', views.store,name='product_by_category'),
#     path('<slug:category_slug>/<slug:product_slug>', views.product_detail,name='product_detail'),
# ]