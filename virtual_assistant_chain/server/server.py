import asyncio
import grpc
from virtual_assistant_chain.server.chat_servicer import ChatServicer
from virtual_assistant_chain.server.bash_servicer import BashServicer
from generated import chat_pb2_grpc
from generated import bash_pb2_grpc

async def serve():
    server = grpc.aio.server()
    chat_pb2_grpc.add_ChatServicer_to_server(ChatServicer(), server)
    bash_pb2_grpc.add_BashServicer_to_server(BashServicer(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    print(f'Starting gRPC server on {listen_addr}...')
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())