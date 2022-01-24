# from django.shortcuts import *
# from django.http import *
# from Store.models.product import Product
# from Store.models.category import Category
#
#
# # by using fbv..
#
# def index(request):
#     products = None
#     categories = Category.get_all_catagories()
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Product.get_all_products_by_categoryid(categoryID)
#     else:
#         products = Product.get_all_products()
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
#     print('You are:', request.session.get('email'))
#     return render(request, 'indexx.html', data)
#
#
# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     else:
#         postData = request.POST
#         first_name = postData.get('firstname')
#         last_name = postData.get('lastname')
#         phone = postData.get('phone')
#         email = postData.get('email')
#         password = postData.get('password')
#         error_message = None
#
#         customer = Customer(first_name=first_name,
#                             last_name=last_name,
#                             phone=phone,
#                             email=email,
#                             password=password)
#         customer.register()
#
#         return render(request, 'signup.html')