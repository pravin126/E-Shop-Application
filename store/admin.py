from django.contrib import admin
from .models.product import Product
from .models.category import Category



class AdminProdct(admin.ModelAdmin):
    list_display=['name','price','desc','category','image']

class AdminCategory(admin.ModelAdmin):
    list_display=['name','id']


admin.site.register(Product,AdminProdct)
admin.site.register(Category,AdminCategory)
