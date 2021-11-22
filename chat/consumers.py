import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

# A consumer is basically a django channel View.

class ChatroomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.pk = self.scope['url_route']['kwargs']['pk']
        await self.channel_layer.group_add()