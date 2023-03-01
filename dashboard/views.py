from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404

from item.models import item

@login_required
def index(request):
    items = item.objects.filter(created_by= request.user)

    return render (request, 'dashboard.html', {
        'items':items
    })


