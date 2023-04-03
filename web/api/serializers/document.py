from rest_framework import serializers
from ..models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'file_path', 'doc_type', 'indexing_status']
