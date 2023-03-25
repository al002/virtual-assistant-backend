from django.db import models
from django.contrib.auth import get_user_model
from .timestamp import TimestampedModel

CustomUser = get_user_model()

class Conversation(TimestampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'conversation'
        ordering = ['-updated_at']