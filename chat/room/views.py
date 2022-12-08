from django.shortcuts import render
from .models import Room, Message
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def chatRooms(request):
    chatrooms = Room.objects.all()

    return render(request, 'room/chatrooms.html', {'chatrooms':chatrooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:10]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})