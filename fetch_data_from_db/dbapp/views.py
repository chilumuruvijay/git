from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect 
from .models import Item 
from .forms import ItemForm 
 
def item_list(request): 
    items = Item.objects.all() 
    return render(request, 'dbapp/item_list.html', {'items': items}) 
 
def item_create(request): 
    if request.method == 'POST': 
        form = ItemForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('item_list')  # Redirect to the item list after saving 
    else: 
        form = ItemForm() 
    return render(request, 'dbapp/item_create.html', {'form': form})