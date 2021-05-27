from django.contrib import admin
from .models import Category,SubCategory,Product,Like
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Like)

# Register your models here.
