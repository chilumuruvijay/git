from django.shortcuts import render 
from .forms import ContactForm 
def contact_view(request): 
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            # Form is valid, handle the data (e.g., save to the database or send an email) 
            name = form.cleaned_data['name'] 
            email = form.cleaned_data['email'] 
            message = form.cleaned_data['message'] 
            # For now, we just display the data as a success message 
            return render(request, 'forms/contact_success.html', {'name': name, 'email': email, 'message': message}) 
        else: 
            print(form.errors) 
    else: 
        form = ContactForm() 
    return render(request, 'forms/contact_form.html', {'form': form})