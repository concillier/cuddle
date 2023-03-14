from django.urls import path

from . import views

app_name = 'inbox'

urlpatterns = [
    path('', views.inbox_view, name='inbox_view'),
    path('new/<int:item_pk>/', views.new_conversation, name= 'new'),
]