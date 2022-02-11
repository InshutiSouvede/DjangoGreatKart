
from django.urls import path

from carts import views 

urlpatterns = [
    path('',views.cart,name='cart')
]
# urlpatterns = [
#     path('', views.store,name='store'),
#     path('<slug:category_slug>/', views.store,name='product_by_category'),
#     path('<slug:category_slug>/<slug:product_slug>', views.product_detail,name='product_detail'),
# ]