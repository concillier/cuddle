from django.shortcuts import render, redirect
from item.models import Category, item
from .forms import SignupForm

# Create your views here.
def index(request): 
    items = item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.filter()
    return render(request, 'index.html', {
        'items': items,
        'categories': categories
        })

def contact(request): 
    return render(request, 'contact.html')


def signup(request): 

    if request.method == 'POST': 
        form = SignupForm(request.POST)

        if form.is_valid(): 
            form.save()

            return redirect('/login/')
    
    else: 
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
        })