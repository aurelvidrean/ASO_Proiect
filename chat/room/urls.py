from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.chatRooms, name="chatRooms"),
    path('<slug:slug>', views.room, name='room')
]