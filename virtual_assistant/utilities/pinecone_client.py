import os
import logging
import pinecone

PINECONE_INDEX_NAME = 'personal-knowledgebase'

def initialize_pinecone():
    try:
        pinecone.init(
            api_key=os.getenv('PINECONE_API_KEY'),
            environment=os.getenv('PINECONE_ENVIRONMENT')
            )

    except Exception as e:
        logging.error(f"An error occurred while initializing Pinecone: {e}")
        return False

    return True
