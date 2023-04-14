from django.apps import AppConfig

from virtual_assistant.utilities import initialize_pinecone

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self) -> None:
        initialize_pinecone()
