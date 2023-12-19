from django.urls import path

from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.AllProdCat, name='AllProdCat'),
    path('<slug:c_slug>/', views.AllProdCat, name='product_cat'),
    path('<slug:c_slug>/<slug:prod_slug>', views.Allprod, name='product')
]
