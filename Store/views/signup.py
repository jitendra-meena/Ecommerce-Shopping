from django.shortcuts import *
from django.http import *
from Store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        error_message = None

        # server validations
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        # Saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': values
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = 'First name is required'
        elif (not customer.last_name):
            error_message = 'Last name is required'
        elif (not customer.phone):
            error_message = 'Mobile number is required'
        elif (not customer.email):
            error_message = 'Email id is required'
        elif (not customer.password):
            error_message = 'Password is required'
        elif customer.isExists():
            error_message = 'Email is Already Register'

        return error_message
