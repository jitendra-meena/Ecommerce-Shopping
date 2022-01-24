from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=57)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    # for save customer data
    def register(self):
        self.save()

    # for user get email id for login

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    # for user email id is alredy exists validation
    def isExists(self):
        if Customer.objects.filter(email= self.email):
            return True
        else:
            return False
