from django.shortcuts import render,redirect
from .forms import ProfileRegistrationForm,LoginForm,PasswordResetForm
from django.contrib.auth import login,authenticate
from django.contrib import messages

def login_view(request):
    
    """
    Checks to see if user is already logged
    if logged in it redirects them 

    This is so to prevent them from logging in when
    they are already logged in
    """

    if request.user.is_authenticated:
        return redirect(to='products')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request,username=username,password=password)

            if not user == None:
                login(request,user)
                messages.success(request,f'You have logged in successfully')
                return redirect(to='products')
                

            else:
                messages.info(request,f'{username.upper()} make sure your credentials are correct')

    else:
        form = LoginForm()
    
    context = {
        'form':form,
    }
    return render(request, 'core/account/login.html',context)



def sign_up_view(request):

    """
    Checks to see if user is already logged
    if logged in it redirects them 

    This is so to prevent them from logging in when
    they are already logged in
    """

    if request.user.is_authenticated:
        return redirect(to='products')

    
    if request.method == "POST":
        form = ProfileRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.refresh_from_db()
            new_user.profile.city = form.cleaned_data.get('city')
            new_user.profile.country = form.cleaned_data.get('country')
            new_user.save()
            messages.success(request,f"Account for {form.cleaned_data.get('username').upper()} as been created successfully")
            return redirect('login')
            
        else:
            messages.info(request,f"There was a problem while creating the your account")
    else:
        form = ProfileRegistrationForm()
    
    context = {
        'form':form,
    }

    return render(request, 'core/account/signup.html',context)