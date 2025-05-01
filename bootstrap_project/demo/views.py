from django.shortcuts import render 
def sample_page(request): 
    return render(request, 'demo/sample.html')