from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import item
from .forms import NewItemForm, EditItemForm

def detail(request, pk): 
    Item = get_object_or_404(item, pk=pk)
    related_items = item.objects.filter(category = Item.category, is_sold= False).exclude(pk=pk)[0:3]

    return render(request, 'detail.html', {
        'item': Item, 
        'related_items': related_items
        })

@login_required
def new(request):

    if request.method == 'POST': 
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid(): 
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
        
    else: 
            form = NewItemForm()

    return render(request, 'form.html', {
        'form': form,
        'title': 'New item',
        })

@login_required
def edit(request, pk):
    Item = get_object_or_404(item, pk=pk, created_by=request.user)

    if request.method == 'POST': 
        form = EditItemForm(request.POST, request.FILES, instance=Item)

        if form.is_valid(): 
            form.save()

            return redirect('item:detail', pk=Item.id)
        
    else: 
            form = EditItemForm(instance=Item)

    return render(request, 'form.html', {
        'form': form,
        'title': 'Edit item',
        })


@login_required
def delete(request,pk):
    Item = get_object_or_404(item, pk=pk, created_by=request.user)
    Item.delete()

    return redirect('dashboard:index')
