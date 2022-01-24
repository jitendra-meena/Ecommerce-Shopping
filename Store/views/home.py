from django.shortcuts import *
from django.http import *
from Store.models.product import Product
from Store.models.category import Category
from django.views import View


# Create your views here. for add to cart

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        print(product)
        return redirect('homepage')

    def get(self, request):
        products = None
        categories = Category.get_all_catagories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('You are:', request.session.get('email'))
        return render(request, 'indexx.html', data)

