import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json

from virtual_assistant_chain.chains.chat.chat import ChatConversation
from ..callbacks.streaming_queue import StreamingWebsocketCallbackHandler

class ChatConsumer(AsyncWebsocketConsumer):
    chat_chain: ChatConversation
    async def connect(self):
        self.queue = asyncio.Queue()
        self.chat_chain = ChatConversation(callbacks=[StreamingWebsocketCallbackHandler(queue=self.queue)])
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        asyncio.create_task(self.send_token_task())
        self.chat_chain.chat(input=message)
    
    async def send_token_task(self):
        while True:
            token = await self.queue.get()
            await self.send(text_data=json.dumps({'reply': token}))
