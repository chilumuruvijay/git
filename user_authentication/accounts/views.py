from django.shortcuts import render, redirect 
from .forms import UserRegistrationForm 
from django.contrib.auth.views import LoginView 
from django.contrib.auth.views import LogoutView 
def register(request): 
    if request.method == 'POST': 
        form = UserRegistrationForm(request.POST) 
        if form.is_valid(): 
            form.save()  # Save the new user 
            return redirect('login')  
    else: 
        form = UserRegistrationForm() 
    return render(request, 'accounts/register.html', {'form': form}) 
class CustomLoginView(LoginView): 
    template_name = 'accounts/login.html' 
 
class CustomLogoutView(LogoutView): 
    next_page = '/' 
 
def home(request): 
    return render(request, 'accounts/home.html') 
 
def logged_in(request): 
    return render(request, 'accounts/logged_in.html')