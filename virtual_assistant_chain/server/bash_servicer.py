import asyncio
from concurrent import futures
import grpc
from generated import bash_pb2 
from generated import bash_pb2_grpc
from virtual_assistant_chain.chains.bash.base import BashChain

bash = BashChain()

class BashServicer(bash_pb2_grpc.BashServicer):
    async def RunBash(self, request: bash_pb2.BashRequest, context: grpc.aio.ServicerContext):
        reply = bash.run(input=request.input)
        for _, char in enumerate(reply):
            yield bash_pb2.BashResponse(reply=char)
