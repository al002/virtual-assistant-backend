from rest_framework import generics
from ..models import Conversation, ChatMessage
from ..serializers import ConversationSerializer

class ConversationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ConversationSerializer

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ConversationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConversationSerializer

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):
        ChatMessage.objects.filter(user=self.request.user, conversation=instance).delete()
        instance.delete()
