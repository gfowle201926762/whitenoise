from django.urls import path

from .views import ChatView, ChatroomView


urlpatterns = [
    path('', ChatView.as_view(), name='chat'),
    path('room/<int:pk>/', ChatroomView.as_view(), name='chatroom')
]