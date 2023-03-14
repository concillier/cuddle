from django.urls import path

from . import views

app_name = 'inbox'

urlpatterns = [

    path('', views.inbox_view, name='inbox_view'),
    path('<int:pk>/', views.inbox_view_details, name='detail'),
    path('new/<int:item_pk>/', views.new_conversation, name= 'new'),
]