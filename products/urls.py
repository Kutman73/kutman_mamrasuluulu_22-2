from django.urls import path
from products.views import *


urlpatterns = (
    path('products/', ProductPage.as_view()),
    path('categorias/', CategoryPage.as_view()),
    path('products/<slug:slug>/<int:pk>/', DetailProductPage.as_view()),
    path('products/create/', product_create_page),
    path('test/', TestPage.as_view())
)
