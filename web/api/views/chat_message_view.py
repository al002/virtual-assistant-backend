from rest_framework import generics
from ..models import ChatMessage, Conversation
from ..serializers import ChatMessageSerializer

class ChatMessageListAPIView(generics.ListAPIView):
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        user = self.request.user
        conversation_id = self.kwargs['conversation_id']
        conversation = Conversation.objects.get(id=conversation_id)
        return ChatMessage.objects.filter(user=user, conversation=conversation)

class ChatMessageDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        user = self.request.user
        conversation_id = self.kwargs['conversation_id']
        conversation = Conversation.objects.get(id=conversation_id)
        return ChatMessage.objects.filter(user=user, conversation=conversation)
