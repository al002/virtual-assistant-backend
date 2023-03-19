import asyncio
import grpc
from generated import chat_pb2
from generated import chat_pb2_grpc

async def run():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        request = chat_pb2.TranslatorChatRequest(language="Spanish", query="你好，世界！")
        result = ""
        async for response in stub.TranslatorChat(request):
            result += response.reply
        print(f'Received: {result}')

if __name__ == '__main__':
    asyncio.run(run())
