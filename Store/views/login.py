from django.shortcuts import *
from django.http import *
from Store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email

                return redirect('homepage')
            else:
                error_message = 'Email or Password is invalid'
        else:
            error_message = 'Email or Password is invalid'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})
