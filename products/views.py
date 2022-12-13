from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from users.utils import get_user_from_request
from products.models import *
from products.forms import *


PAGINATION_LIMIT = 10


class ProductPage(ListView):
    model = Product
    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        return {
            'products': kwargs['products'],
            'user': get_user_from_request(self.request),
            'category_id': kwargs['category_id'],
            'max_page': range(1, kwargs['max_page']+1),
        }

    def get(self, requests, *args, **kwargs):
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
            } for product in products]

            max_page = round(products.__len__() / PAGINATION_LIMIT)
            products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

            return render(requests, self.template_name, context=self.get_context_data(
                products=products,
                category_id=category_id,
                max_page=max_page
            ))

class CategoryPage(ListView):
    model = Category
    template_name = 'categorias/categorias.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'categorias': self.get_queryset(),
            'user': get_user_from_request(self.request)
        }


# def detail_product_page(requests, id, title):
#     if requests.method == 'GET':
#         product = Product.objects.get(id=id, title=title)
#         review = Review.objects.filter(product_id=id, product__title=title)
#
#         data = {
#             'product': product,
#             'categorias': product.categorias.all(),
#             'reviews': review,
#             'form': ReviewCreateForm,
#             'user': get_user_from_request(requests)
#         }
#         return render(requests, 'products/detail.html', context=data)
#
#     if requests.method == 'POST':
#         form = ReviewCreateForm(data=requests.POST)
#
#         if form.is_valid():
#             Review.objects.create(
#                 author_id=3,
#                 text=form.cleaned_data.get('text'),
#                 product_id=id
#             )
#             return redirect(f'/products/{id}/')
#
#         else:
#             product = Product.objects.get(id=id, title=title)
#             review = Review.objects.filter(product_id=id, product__title=title)
#
#             data = {
#                 'product': product,
#                 'categorias': product.categorias.all(),
#                 'reviews': review,
#                 'form': form,
#                 'user': get_user_from_request(requests)
#             }
#             return render(requests, 'products/create.html', context=data)


class DetailProductPage(DetailView):
    model = Product
    # context_object_name = 'product'
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailProductPage, self).get_context_data(**kwargs)
        context['form'] = ReviewCreateForm
        # context['categorias'] = Category.objects.all()
        context['reviews'] = Review.objects.all()
        return context

    def post(self, request, **kwargs):
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                author_id=request.user.id if not request.user.is_anonymous else 3,
                text=form.cleaned_data.get('text'),
                product_id=kwargs['pk']
            )
            return redirect(f'/products/{kwargs["slug"]}/{kwargs["pk"]}/')

        else:
            products = Product.objects.get(id=self.model.pk)
            reviews = Review.objects.filter(product_id=self.model.pk)

            data = {
                'product': products,
                'categorias': products.categorias.all(),
                'reviews': reviews,
                'form': form
            }
            return render(request, self.template_name, context=data)


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


class ProductCreatePage(View):
    template_name = 'products/create.html'

    def get(self, request, *args, **kwargs):
        form = ProductCreateForm(request.POST, request.FILES)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(
                author_id=request.user.id if not request.user.is_anonymous else 2,
                title=form.cleaned_data.get('title'),
                image=form.cleaned_data.get('image'),
                description=form.cleaned_data.get('description'),
                publication_date=form.cleaned_data.get('publication_date'),
            )
            return redirect('/posts/')

        return render(request, self.template_name, {'form': form})


class TestPage(ListView):
    template_name = 'layouts/main.html'

    def get_queryset(self):
        pass
