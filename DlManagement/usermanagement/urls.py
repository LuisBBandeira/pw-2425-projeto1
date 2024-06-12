from django.urls import path 
from .views import IndexView , LogOut ,SignIn , SignUp


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('sign_in/', SignIn.sign_in, name='sign_in'),
    path('sign_up/', SignUp.sign_up, name='sign_up'),
    path('log_out/', LogOut.log_out, name='sign_out'),
]