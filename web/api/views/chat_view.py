from typing import Any
from django.http import StreamingHttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from virtual_assistant_chain.chains.chat.chat import ChatConversation

class ChatView(APIView):
    chat: ChatConversation

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.chat = ChatConversation()

    def post(self, request):
        input = request.data.get('input')

        if input is not None:
            response = StreamingHttpResponse(self.event_stream(input), content_type="text/event-stream")
            response['Cache-Control'] = 'no-cache'
            # response['Connection'] = 'keep-alive'
            return response
        else:
            return Response({"detail": "Input is required."}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return StreamingHttpResponse(self.event_stream(), content_type="text/event-stream")

    def event_stream(self, input):
        reply = self.chat.chat(input=input)
        yield f"{json.dumps(reply)}\n\n"
