from django.shortcuts import render, redirect, get_object_or_404 
from .models import Record 
from .forms import RecordForm 
 
def record_list(request): 
    records = Record.objects.all() 
    return render(request, 'crud_app/record_list.html', {'records': records}) 
 
def record_create(request): 
    if request.method == 'POST': 
        form = RecordForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('record_list') 
    else: 
        form = RecordForm() 
    return render(request, 'crud_app/record_form.html', {'form': form, 
'action': 'Create'}) 
 
def record_update(request, pk): 
    record = get_object_or_404(Record, pk=pk) 
    if request.method == 'POST': 
        form = RecordForm(request.POST, instance=record) 
        if form.is_valid(): 
            form.save() 
            return redirect('record_list') 
    else: 
        form = RecordForm(instance=record) 
    return render(request, 'crud_app/record_form.html', {'form': form, 
'action': 'Update'}) 
 
def record_delete(request, pk): 
    record = get_object_or_404(Record, pk=pk) 
    if request.method == 'POST': 
        record.delete() 
        return redirect('record_list') 
    return render(request, 'crud_app/record_delete.html', {'record': record}) 