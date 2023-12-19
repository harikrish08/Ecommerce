from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:prod_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:prod_id>/', views.cart_delete, name='cart_delete'),
    path('cart_remove/<int:prod_id>/', views.full_delete, name='full_delete')
]
