from django.shortcuts import render, get_object_or_404
from .models import item

def detail(request, pk): 
    Item = get_object_or_404(item, pk=pk)
    related_items = item.objects.filter(category = Item.category, is_sold= False).exclude(pk=pk)[0:3]

    return render(request, 'detail.html', {
        'item': Item, 
        'related_items': related_items
        })
