from django.shortcuts import render
from django.views import View

from .models import Chatroom


# Create your views here.

class ChatView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'chat/chat.html', context)

class ChatroomView(View):
    def get(self, request, pk, *args, **kwargs):
        room = Chatroom.objects.get(pk=pk)
        context = {}
        return render(request, 'chat/chatroom.html', context)