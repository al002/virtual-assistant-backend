from django.db import models
from django.contrib.auth import get_user_model
from .conversation import Conversation
from .timestamp import TimestampedModel

CustomUser = get_user_model()

class ChatMessage(TimestampedModel):

    class MessageRole(models.TextChoices):
        AI = 'AI'
        Human = 'Human'

    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    chat_session = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    message = models.TextField()
    message_role = models.CharField(max_length=255, choices=MessageRole.choices)
    message_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'chat_message'
        ordering = ['-updated_at']