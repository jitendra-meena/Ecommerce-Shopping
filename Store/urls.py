from django.contrib import admin
from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login

# For CBV........
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login')

]

# For FBV........

# from .views import index, signup
#
# urlpatterns = [
#     path('', index, name='homepage'),
#     path('signup', signup, name='signup'),
#
# ]
