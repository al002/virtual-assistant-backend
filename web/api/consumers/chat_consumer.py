import asyncio
import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from virtual_assistant.chains.chat.chat import ChatConversation
from ..callbacks.streaming_queue import StreamingWebsocketCallbackHandler
from ..models.chat_message import ChatMessage
from ..models.conversation import Conversation

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.conversation_chains = {}
        self.conversation_queues = {}
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        conversation_id = text_data_json['conversation_id']
        if conversation_id not in self.conversation_queues:
            self.conversation_queues[conversation_id] = asyncio.Queue()

        if conversation_id not in self.conversation_chains:
            self.conversation_chains[conversation_id] = ChatConversation(callbacks=[StreamingWebsocketCallbackHandler(queue=self.conversation_queues[conversation_id])])

        chain = self.conversation_chains.get(conversation_id)
        asyncio.create_task(self.handle_queue_message_task(conversation_id))
        reply = chain.chat(input=message)
        await self.save_message(message=message, reply=reply, conversation_id=conversation_id)
    
    async def handle_queue_message_task(self, conversation_id: str):
        while True:
            for name, queue in self.conversation_queues.items():
                if name == conversation_id:
                    info = await queue.get()
                    if info['type'] == 'llm_new_token':
                        await self.send(text_data=json.dumps({'conversation_id': conversation_id, 'msg_type': 'reply_new_token', 'token': info['token']}))
                    elif info['type'] == 'llm_end':
                        await self.send(text_data=json.dumps({'conversation_id': conversation_id, 'msg_type': 'reply_end', 'token': ''}))

    @database_sync_to_async
    def save_message(self, message: str, reply: str, conversation_id: str):
        conversation = Conversation.objects.get(id=conversation_id)
        chat_message = ChatMessage(message=message, message_role="Human", message_type="text", conversation=conversation, user=self.scope['user'])
        chat_message.save()

        reply_message = ChatMessage(message=reply, message_role="AI", message_type="text", conversation=conversation, user=self.scope['user'])
        reply_message.save()        
