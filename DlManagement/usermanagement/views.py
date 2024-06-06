from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render ,redirect
from django.views.generic import TemplateView
from .forms import LoginForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'

class LogOut():
    def log_out(request):
        logout(request)
        return redirect('sign_in')
    
class SignIn():
    def sign_in(request):
        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect('home')
        else:
            form = LoginForm()
        return render(request, 'sign_in.html', {'form': form})
    
class SignUp():
    def sign_up(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
        else:
            form = RegisterForm()
        return render(request, 'sign_up.html', {'form': form})