from typing import List

from langchain.docstore.document import Document
from langchain.vectorstores import Milvus
from langchain.embeddings import OpenAIEmbeddings

class MilvusClient:
    _instance = None

    @staticmethod
    def get_instance():
        if MilvusClient._instance is None:
            MilvusClient._instance = MilvusClient.__MilvusClient()
        return MilvusClient._instance

    class __MilvusClient:
        client: Milvus 

        @classmethod
        def from_documents(self, documents: List[Document]) -> Milvus:
            return Milvus.from_documents(
                embedding=OpenAIEmbeddings(),
                documents=documents,
                connection_args={"host": "127.0.0.1", "port": "19530"},
            )


milvus_client = MilvusClient.get_instance()