from django.urls import path, re_path

from .consumers import ChatroomConsumer

ws_urlpatterns = [
    path('ws/chat/<int:pk>/', ChatroomConsumer.as_asgi())
]