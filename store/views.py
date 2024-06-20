from django.shortcuts import render
from .models.product import Product
from .models.category import Category
# Create your views here.
def index(request):
    product=Product.get_all_products();
    category=Category.get_all_categories();
    data={}
    data['product']=product
    data['category']=category
    return render(request,'index.html',data)
    # return render (request,'orders/orders.html')