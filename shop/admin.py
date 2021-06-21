from django.contrib import admin
from .models import Category,SubCategory,Product,Like,Orders
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Like)
admin.site.register(Orders)

# Register your models here.
