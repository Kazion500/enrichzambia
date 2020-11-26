from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import sign_up_view, login_view

from accounts.forms import PasswordResetCustomForm, PasswordResetConfirmForm
from .views import (
    home_view,
    contact_view,
    about_view,
    product_registration_view,
    products,
    product_view,
    profile_view,
    courses_view,
    find_your_employee_view,
    edit_profile_view,
    search_view,
    category_search_view,
    plan_view,

)

urlpatterns = [
    path('', home_view, name='home'),
    path('contact-us/', contact_view, name='contact'),
    path('about-us/', about_view, name='about'),
    path('courses/', courses_view, name='course'),
    path('plan/', plan_view, name='plan'),
    path('query/', search_view, name='search'),
    path('products/', products, name='products'),
    path('category/<str:category>', category_search_view, name='category_search'),
    path('product-registration/', product_registration_view,
         name='product-registration'),
    path('find-your-employer/', find_your_employee_view, name='find-your-employer'),


    path('product/<str:pk>/', product_view, name='product'),
    path('profile/<str:username>/', profile_view, name='profile'),
    path('profile/edit/<str:username>', edit_profile_view, name='edit-profile'),



    path('signup/', sign_up_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.
         as_view(template_name='core/account/password_reset_form.html',
                 form_class=PasswordResetCustomForm), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.
         as_view(template_name='core/account/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.
         as_view(template_name='core/account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.
         as_view(template_name='core/account/password_reset_confirm.html',
                 form_class=PasswordResetConfirmForm), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.
         as_view(template_name='core/account/password_reset_complete.html'),
         name='password_reset_complete'),
]
