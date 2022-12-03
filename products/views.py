from django.shortcuts import render, redirect
from users.utils import get_user_from_request
from products.models import *
from products.forms import *


# Create your views here.
# Function Based Views
PAGINATION_LIMIT = 1

def Product_page(requests):
    if requests.method == 'GET':
        category_id = requests.GET.get('category_id')
        search_text = requests.GET.get('search')
        page = int(requests.GET.get('page', 1))

        if category_id:
            products = Product.objects.filter(categorias__in=[category_id])
        else:
            products = Product.objects.all()

        if search_text:
            products = products.filter(title__icontains=search_text)

        products = [{
            'cover': product.product_cover,
            'title': product.title,
            'description': product.description,
            'categorias': product.categorias.all()
        }for product in products]

        max_page = round(products.__len__() / PAGINATION_LIMIT)
        products = products[PAGINATION_LIMIT * (page-1):PAGINATION_LIMIT * page]

        data = {
            'products': products,
            'user': get_user_from_request(requests),
            'category_id': category_id,
            'max_page': range(1, max_page)
        }
        return render(requests, 'products/products.html', context=data)


def Category_page(requests, **kwargs):
    if requests.method == 'GET':
        categorias = Category.objects.all()

        data = {
            'categorias': categorias,
            'user': get_user_from_request(requests)
        }
        return render(requests, 'categorias/categorias.html', context=data)


def detail_product_page(requests, id, title):
    if requests.method == 'GET':
        product = Product.objects.get(id=id, title=title)
        review = Review.objects.filter(product_id=id, product__title=title)

        data = {
            'product': product,
            'categorias': product.categorias.all(),
            'reviews': review,
            'form': ReviewCreateForm,
            'user': get_user_from_request(requests)
        }
        return render(requests, 'products/detail.html', context=data)

    if requests.method == 'POST':
        form = ReviewCreateForm(data=requests.POST)

        if form.is_valid():
            Review.objects.create(
                author_id=3,
                text=form.cleaned_data.get('text'),
                product_id=id
            )
            return redirect(f'/products/{id}/')

        else:
            product = Product.objects.get(id=id, title=title)
            review = Review.objects.filter(product_id=id, product__title=title)

            data = {
                'product': product,
                'categorias': product.categorias.all(),
                'reviews': review,
                'form': form,
                'user': get_user_from_request(requests)
            }
            return render(requests, 'products/create.html', context=data)


def product_create_page(requests):
    if requests.method == 'GET':
        data = {
            'form': ProductCreateForm,
            'user': get_user_from_request(requests)
        }
        return render(requests, 'products/create.html', context=data)

    if requests.method == 'POST':
        form = ProductCreateForm(data=requests.POST)

        if form.is_valid():
            Product.objects.create(
                author_id=4,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description')
            )
            return redirect('/products')

        else:
            data = {
                'form': form,
                'user': get_user_from_request(requests)
            }
            return render(requests, 'products/create.html', context=data)


def test_page(requests):
    if requests.method == 'GET':
        return render(requests, 'layouts/main2.html')
