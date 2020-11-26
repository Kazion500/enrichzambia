from .models import Review,Product
from .forms import (
    ReviewForm,
)


def rates_view(request):
    review = Review.objects.all()
    return { 'review':review }


def product_rates_view(request):
    products = Product.objects.all()
    return { 'product':products }


