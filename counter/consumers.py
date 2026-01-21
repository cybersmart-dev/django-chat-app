import json, random
import time
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class CounterConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.user = self.scope["user"]
        
        if not self.user.is_authenticated:
            await self.close()
            return
            
        self.room_group_name = "test"
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
                
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        
        await self.channel_layer.group_send(
            self.room_group_name,{
                "type":"chat_message",
                "message":message,
                "sender": self.user.username
            }
        )
        
    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]
        
        await self.send(text_data=json.dumps({
                "type":"chat",
                "message":message,
                "sender": sender
            }))
        