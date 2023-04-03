from langchain.document_loaders import WebBaseLoader
from celery.exceptions import MaxRetriesExceededError
from web.celery import app

def index_document(doc_id, doc_type, file_path):
    if doc_type == 'url':
        loader = WebBaseLoader([file_path])
        docs = loader.load()
        docs

@app.task(bind=True, max_retries=3, default_retry_delay=60)
def index_document_task(self, doc_id, doc_type, file_path):
    try:
        index_document(doc_id, doc_type, file_path)
    except Exception as e:
        try:
            # Retry the task with a delay
            self.retry(countdown=self.default_retry_delay, exc=e)
        except MaxRetriesExceededError:
            # Log the error or notify the admin after reaching the maximum retry attempts
            pass