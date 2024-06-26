from django.urls import path 
from .views import IndexView , LogOut ,SignIn , SignUp
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('sign_in/', SignIn.sign_in, name='sign_in'),
    path('sign_up/', SignUp.sign_up, name='sign_up'),
    path('log_out/', LogOut.log_out, name='sign_out'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]