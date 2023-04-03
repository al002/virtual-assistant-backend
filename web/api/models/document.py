from django.db import models
from django.contrib.auth.models import User
from .timestamp import TimestampedModel

class IndexingStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    INDEXING = 'indexing', 'Indexing'
    SUCCESS = 'success', 'Success'
    FAILED = 'failed', 'Failed'

class Document(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=50)
    file_path = models.CharField(max_length=255)
    indexing_status = models.CharField(
        max_length=10,
        choices=IndexingStatus.choices,
        default=IndexingStatus.PENDING
    )
