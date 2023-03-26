from rest_framework import serializers
from ..models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['id', 'message', 'user', 'conversation', 'message_role', 'message_type', 'created_at']
        read_only_fields = ['user', 'message_role']
