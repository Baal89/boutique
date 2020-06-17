from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show individual product details"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show all products, including sorting and search queries """

    products = get_object_or_404(Product, product_id)

    context = {
        'products': products,
    }

    return render(request, 'products/product_detail.html', context)

