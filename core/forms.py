from django import forms
from .models import (
    Product,
    Profile,
    Plan,
    Category,
    Review,
)
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.core.exceptions import ValidationError


class ProductModelForm(forms.ModelForm):

    category = forms.ModelChoiceField(Category.objects.all(), widget=forms.Select(
        attrs={"class": "form-style"}), empty_label='Select category')

    class Meta:
        model = Product
        fields = ['name', 'category', 'actual_price',
                  'previous_price', 'product_type', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-style", "placeholder": "Product name"}),
            'actual_price': forms.TextInput(attrs={"class": "form-style", "placeholder": "Price"}),
            'previous_price': forms.TextInput(attrs={"class": "form-style", "placeholder": "Previous Price (Optional)"}),
            'product_type': forms.Select(attrs={"class": "form-style"}),
            'description': forms.Textarea(
                attrs={'rows': '7', 'cols': '30', "class": "form-style", "placeholder": "Describe your product or service"}),
            'image': forms.FileInput(attrs={"class": "form-style"})

        }


class UpdateProfileForm(forms.ModelForm):

    phone = forms.CharField(help_text='Add Country Code e.g +260', widget=forms.TextInput(
        attrs={
            'class': "form-style",
            'placeholder': 'Enter Your phone number'
        }
    ), required=False)
    # plan = forms.ModelChoiceField(
    #     queryset=Plan.objects.all(), empty_label='Choose a plan', widget=forms.Select(attrs={'class': "form-style"})
    # )
    country = CountryField(blank_label='(Select country)').formfield(
        widget=CountrySelectWidget(
            attrs={"class": "form-style"}
        ),
        required=False
    )
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-style",
            'placeholder': 'Enter Your city'
        }
    ), required=False)
    business_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-style",
            'placeholder': 'Enter Your Business name'
        }
    ), required=False)

    business_location = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-style",
            'placeholder': 'Enter Your Business location'
        }
    ), required=False)

    image = forms.ImageField(widget=forms.FileInput(
        attrs={
            'class': "form-style",
        }
    ), required=False)

    class Meta:
        model = Profile
        fields = [
            'phone',
            'country',
            'city',
            'business_name',
            'business_location',
            'image',
            'user',
            'bio',
            'deliver'
        ]
        widgets = {
            'user': forms.HiddenInput(
                attrs={
                    'class': "form-style",
                    "style": "display:none",
                }
            ),

            'deliver': forms.Select(
                attrs={
                    'class': 'form-style',
                },
            ),

            'bio': forms.Textarea(
                attrs={
                    'cols': '20',
                    'rows': '6',
                    'class': "form-style",
                    'placeholder': "Write Something about Company"
                }
            )
        }


class CoverUpload(forms.Form):
    cover_image = forms.ImageField(
        widget=forms.FileInput(attrs={"id": "cover_img"}))


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "fye-input", "placeholder": "Fullname"}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "fye-input", "placeholder": "E-mail Address"}))
    subject = forms.CharField(
        widget=forms.TextInput(attrs={"class": "fye-input", "placeholder": "Subject"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "fye-input", "cols": "5", "rows": "5", "placeholder": "Message"}))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'comment', 'rates']
        widgets = {
            'user': forms.HiddenInput(),
            'comment': forms.Textarea(
                attrs={"cols": "19", "rows": "3", "placeholder": "How was your Experice with us",
                       "style": "padding: .5em; width:60%"}),
            'rates': forms.HiddenInput(),
        }
