from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_countries.fields import CountryField
import uuid


DELIVER = (
    ('', 'Do you Deliver?'),
    ('Y', 'Yes'),
    ('N', 'No'),
)
PLAN_OPTION = (
    ('Mwaiseni - FREE', 'Mwaiseni'),
    ('Kadyonko - K2/DAY', 'Kadyonko'),
    ('Mukolwe - K15/Month', 'Mukolwe'),
)

IS_SERVICE = (
    ('', 'Product or Service'),
    ('Product', 'Product'),
    ('Service', 'Service '),
    ('Both', 'Both '),
)


class Plan(models.Model):
    name = models.CharField(
        max_length=50, choices=PLAN_OPTION, default='Mwaiseni - FREE')
    price = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=1000)

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    user_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(
        max_length=50, help_text='Must have a country code', null=True, blank=True)
    country = CountryField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    business_name = models.CharField(max_length=100, null=True, blank=True)
    business_location = models.CharField(max_length=50, null=True, blank=True)
    deliver = models.CharField(
        max_length=20, choices=DELIVER, null=True, blank=True)
    plan = models.OneToOneField(
        Plan, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(max_length=400, null=True,
                           blank=True, help_text='Maximum 300 Words')
    image = models.ImageField(
        upload_to='product', default='product/default.png')
    cover_image = models.ImageField(
        upload_to='cover', default='cover/default.jpg')
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        width = 200
        height = 200

        if img.width > width or img.height > height:
            output = (width, height)
            img.thumbnail(output)
            img.save(self.image.path)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Review(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    comment = models.TextField(max_length=200)
    rates = models.PositiveIntegerField(default=0)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.rates)


class Product(models.Model):
    product_uuid = models.UUIDField(
        primary_key=True, blank=True, default=uuid.uuid4, editable=False)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    actual_price = models.CharField(max_length=15)
    previous_price = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='product')
    approved = models.BooleanField(default=False)
    top_sale = models.BooleanField(default=False)
    reviews = models.ForeignKey(
        Review, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    product_type = models.CharField(max_length=20, choices=IS_SERVICE)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        width = 500
        height = 400
        if img.width > width or img.height > height:
            output = (width, height)
            img.thumbnail(output)
            img.save(self.image.path)
