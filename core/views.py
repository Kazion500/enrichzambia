from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mass_mail, send_mail


from .models import (
    Product,
    Profile,
    Category,
    Review,
    Plan,
)

from .forms import (
    ProductModelForm,
    UpdateProfileForm,
    CoverUpload,
    ContactForm,
    ReviewForm,
)


def home_view(request):
    if request.user.is_authenticated and request.user.profile.is_seller:
        return redirect('products')
    top_sale_products = Product.objects.filter(
        top_sale=True, approved=True)[:8]
    reviews = Review.objects.all()

    context = {
        'top_sale_products': top_sale_products,
        'reviews': reviews
    }

    return render(request, 'core/pages/index.html', context)


def about_view(request):
    return render(request, 'core/pages/about.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data.get("fullname")
            email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            if len(fullname) > 6:

                send_mail(subject=subject,
                          message=message,
                          from_email=email,
                          recipient_list=['patrickckabwe@gmail.com'],
                          html_message=f"Full Name: {fullname} <br> From :{email} <br><br> Message : {message}"
                          )
                messages.success(
                    request, f'We have recieved your email, We will get in touch with you as soon as possible')
                return redirect('contact')
            else:
                messages.error(
                    request, f'Make sure you entered a full name e.g John Doe')
                return redirect('contact')
        else:
            messages.info(
                request, f'Check your input fields Make sure all fields are filled')
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        "form": form,
    }
    return render(request, 'core/pages/contact.html', context)


def products(request):
    approved_products = Product.objects.filter(approved=True)
    top_sale_products = Product.objects.filter(top_sale=True, approved=True)
    categories = Category.objects.all()

    context = {
        'approved_products': approved_products,
        'top_sale_products': top_sale_products,
        'categories': categories,
    }

    return render(request, 'core/pages/products.html', context)


def category_search_view(request, category):
    approved_products = Product.objects.filter(
        approved=True, category__name__iexact=category)
    categories = Category.objects.all()

    context = {
        'approved_products': approved_products,
        'categories': categories,
    }

    return render(request, 'core/pages/category_search.html', context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk__iexact=pk)
    related_products = Product.objects.filter(
        category__name=product.category, approved=True).exclude(pk=pk)

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'core/pages/product.html', context)


@login_required(login_url='products')
def product_registration_view(request):
    """
    Checks to see if logged in user is a seller if so they will
    access the page

    This is so to prevent anyuser from adding products
    """

    if not request.user.profile.is_seller:
        return redirect('products')

    """
    Checks to see if logged in user has products < 1

    This is so to prevent user from adding products just after
    registration
    """
    if request.user.profile.product_set.all().count() < 1:
        return redirect('products')

    seller_auth = request.user
    products = Product.objects.filter(seller__user=seller_auth)
    categories = Category.objects.all()

    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.profile.is_seller:
                product_obj = form.save(commit=False)
                product_obj.seller = products[0].seller
                product_obj.save()
                messages.success(
                    request, f"You have Successfully Registered {form.cleaned_data.get('name')},Please Wait While we Check your {form.cleaned_data.get('product_type')}")
                return redirect('product-registration')
        else:
            messages.info(request, f"Check you inputs, File must be image")
            return redirect('product-registration')
    else:
        form = ProductModelForm()

    context = {
        'products': products,
        'seller_auth': seller_auth,
        'seller_auth': seller_auth,
        'form': form,
        'categories': categories,
    }

    return render(request, 'core/pages/product-registration.html', context)


def find_your_employee_view(request):
    context = {}
    return render(request, 'core/pages/find-your-employer.html', context)


def courses_view(request):
    context = {}
    return render(request, 'core/pages/courses.html', context)


def plan_view(request):
    plans = Plan.objects.all()
    # plan = Plan.objects.get(name=plan)
    context = {
        'plans': plans,
        # 'plan': plan,
    }
    return render(request, 'core/pages/plan.html', context)


def profile_view(request, username):
    seller = get_object_or_404(Profile, user__username__exact=username)

    if request.method == "POST":
        form = CoverUpload(request.POST, request.FILES)
        if form.is_valid():
            cover_image = form.cleaned_data.get('cover_image')
            profile = get_object_or_404(
                Profile, user__username__exact=username)
            profile.cover_image.delete()
            profile.cover_image = cover_image
            profile.save()
            messages.success(request, f'Successfully updated your Cover Image')
            return redirect('profile', seller.user.username)
        else:
            messages.info(request, f'Image must be less then 20mb')
            return redirect('profile', seller.user.username)
    else:
        form = CoverUpload()

    # Handle reviews via Ajax Call
    # if request.is_ajax():
    #     form_rate = ReviewForm()
    #     if form_rate.is_valid():
    #         pass
    # else:
    #     form_rate = ReviewForm()

    context = {
        'form': form,
        # 'form_rate': form_rate,
        'seller': seller,
    }
    return render(request, 'core/pages/profile.html', context)


@login_required(login_url='login')
def edit_profile_view(request, username):
    seller = get_object_or_404(Profile, user__username=username)
    if not request.user.profile.is_seller:
        return redirect('products')

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=seller)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated your profile')
            return redirect('profile', seller.user.username)
        else:
            messages.info(request, f'Please check your credentials')
    else:
        form = UpdateProfileForm(instance=seller)

    context = {
        'seller': seller,
        'form': form,
    }
    return render(request, 'core/pages/update-profile.html', context)


def search_view(request):

    try:
        q = request.GET.get('search')
        if q == '':
            return redirect('products')
        products = Product.objects.filter(
            Q(name__icontains=q) |
            Q(category__name__icontains=q)
        )
        approved_products = []
        for product in products:
            if product.approved:
                approved_products.append(product)
    except (ValueError, UnboundLocalError):
        approved_products = []

    context = {
        'products': approved_products,
        'products_returned': len(approved_products),
        'search_result': q
    }
    return render(request, 'core/pages/search-results.html', context)
