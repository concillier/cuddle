from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import item
from .models import Conversation
from .forms import ConversationMessageForm

# Create your views here.

@login_required
def new_conversation(request, item_pk): 

    Item = get_object_or_404(item, pk= item_pk)

    if Item.created_by == request.user: 
        return redirect('dashboard: dashboard')
    
    conversations = Conversation.objects.filter(itemm = Item).filter(members__in=[request.user.id])

    if conversations: 
        pass #redirect to conversation

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(itemm = Item)
            conversation.members.add(request.user)
            conversation.members.add(Item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
        
    else: 
        form = ConversationMessageForm()

    return render(request, 'new.html', {
        'form': form
    })


@login_required
def inbox_view(request): 
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'inbox.html', {
        'conversations': conversations
    })





