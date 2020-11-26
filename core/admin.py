from django.contrib import admin

from .models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Plan)
admin.site.register(Profile)
admin.site.register(Review)