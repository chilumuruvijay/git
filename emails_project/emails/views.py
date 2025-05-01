from django.shortcuts import render, redirect 
from django.core.mail import send_mail 
from .forms import EmailForm 
from django.contrib import messages 
def send_email(request): 
    if request.method == 'POST': 
        form = EmailForm(request.POST) 
        if form.is_valid(): 
            recipient = form.cleaned_data['recipient'] 
            subject = form.cleaned_data['subject'] 
            message = form.cleaned_data['message'] 
            # Send the email 
            send_mail( 
                subject, 
                message, 
                'your-email@gmail.com',  # The sender's email 
                [recipient],  # The recipient's email 
            ) 
            # Show a success message 
            messages.success(request, 'Email sent successfully!') 
            return redirect('send_email')  # Redirect to the email form page 
    else: 
        form = EmailForm() 
    return render(request, 'emails\send_email.html', {'form': form}) 
