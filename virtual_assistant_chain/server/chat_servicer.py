import asyncio
from concurrent import futures
import grpc
from generated import chat_pb2
from generated import chat_pb2_grpc
from virtual_assistant_chain.chains.chat.chat import ChatConversation

chat = ChatConversation()

class ChatServicer(chat_pb2_grpc.ChatServicer):
    async def Chat(self, request: chat_pb2.ChatRequest, context: grpc.aio.ServicerContext):
        reply = chat.chat(input=request.input)
        for _, char in enumerate(reply):
            yield chat_pb2.ChatResponse(reply=char)

    async def CodeGenerationChat(self, request: chat_pb2.CodeGenerationChatRequest, context: grpc.aio.ServicerContext):
        reply = chat.chat_with_type(type="code_generation", position=request.position, tech_stacks=request.tech_stacks, query=request.query)
        for _, char in enumerate(reply):
            yield chat_pb2.ChatResponse(reply=char)

    async def TranslatorChat(self, request: chat_pb2.TranslatorChatRequest, context: grpc.aio.ServicerContext):
        reply = chat.chat_with_type(type="translator", language=request.language, query=request.query)
        for _, char in enumerate(reply):
            yield chat_pb2.ChatResponse(reply=char)
