from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
 
def home_view(request): 
    return render(request, 'authentication/home.html') 
 
def register_view(request):
     if request.method == 'POST': 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            login(request, user) 
            messages.success(request, "Registration successful.") 
            return redirect('dashboard') 
        messages.error(request, "Unsuccessful registration. Invalid information.")
     else:  # Fixed indentation here
        form = UserCreationForm()  
     return render(request, 'authentication/register.html', {'form': form}) 

def login_view(request): 
    if request.method == 'POST': 
        form = AuthenticationForm(request, data=request.POST) 
        if form.is_valid(): 
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password') 
            user = authenticate(username=username, password=password) 
            if user is not None: 
                login(request, user) 
                messages.success(request, f"You are logged in as {username}.") 
                return redirect('dashboard') 
            else: 
                messages.error(request, "Invalid username or password.") 
        else: 
            messages.error(request, "Invalid username or password.") 
    form = AuthenticationForm() 
    return render(request, 'authentication/login.html', {'form': form}) 
 
def logout_view(request): 
    logout(request) 
    messages.success(request, "You have successfully logged out.") 
    return redirect('home') 
 
@login_required 
def dashboard_view(request): 
    return render(request, 'authentication/dashboard.html')