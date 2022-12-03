from django.urls import path
from products.views import *


urlpatterns = [
    path('products/', Product_page),
    path('categorias/', Category_page),
    path('products/<str:title>/<int:id>/', detail_product_page),
    path('products/create/', product_create_page),
    path('test/', test_page)
]
