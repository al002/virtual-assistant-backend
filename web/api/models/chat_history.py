from django.db import models

class ChatHistory(models.Model):

    class MessageRole(models.TextChoices):
        AI = 'AI'
        Human = 'Human'

    message = models.TextField()
    message_role = models.CharField(max_length=255, choices=MessageRole.choices)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat_history'
        ordering = ['-timestamp']