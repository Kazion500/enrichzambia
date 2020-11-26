from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget



class ProfileRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class":"form-auth",'placeholder':'Enter Your Username'})
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class":"form-auth",'placeholder':'Enter Your E-mail Address'})
    )
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class":"form-auth",'placeholder':'Enter Your Password'})
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class":"form-auth",'placeholder':'Confirm Your Password'})
    )
    country = CountryField(blank_label='(Select country)').formfield( 
        widget=CountrySelectWidget(attrs={"class": "form-auth"})
    )
    city = forms.CharField(widget=forms.TextInput(
        attrs={'class':"form-auth",'placeholder':'Enter Your city'}
    ))

    class Meta:
        model = User
        fields = ['username','country','email','city','password1','password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-auth",
            "placeholder":'Enter Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class":"form-auth",
            "placeholder":'Enter Password'
        }
    ))

class PasswordResetCustomForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder" : "Enter Your E-mail Address",
            "class":"form-auth",
            }))

class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput())
    new_password2 = forms.CharField(
        widget=forms.PasswordInput())
    