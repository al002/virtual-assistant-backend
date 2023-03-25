from rest_framework import serializers
from ..models import Conversation

class ConversationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'title', 'user']
