import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
import uuid

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

class FreenMemory:
    def __init__(self, qdrant_url=None, api_key=None, collection="freen_memories"):
        url = qdrant_url or QDRANT_URL
        key = api_key if api_key is not None else QDRANT_API_KEY
        key = key or None  # allow local/no-auth
        self.client = QdrantClient(url=url, api_key=key, timeout=30.0)
        self.collection = collection

        # Create collection if it doesn't exist
        try:
            self.client.get_collection(self.collection)
        except Exception:
            # Create only if missing (non-destructive)
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config={"size": 1536, "distance": "Cosine"},
            )

    def add_memory(self, text):
        point = PointStruct(
            id=str(uuid.uuid4()),
            vector=[0.0] * 1536,  # Placeholder until we embed text
            payload={"text": text},
        )
        self.client.upsert(collection_name=self.collection, points=[point])

    def get_relevant_memories(self, query, top_k=3):
        try:
            search_result = self.client.scroll(collection_name=self.collection, limit=top_k)
            memories = [{"payload": p.payload} for p in search_result[0]]
            return memories
        except Exception as e:
            print("Error fetching memories:", e)
            return []
