from rest_framework import generics
from ..models import Document
from ..serializers import DocumentSerializer
from ..utils import index_document_task

class DocumentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)

        # Index the document content to Milvus using a Celery task
        index_document_task.delay(doc_id=instance.id, doc_type=instance.doc_type, file_path=instance.file_path)

class DocumentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)
