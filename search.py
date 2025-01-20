from qdrant_client import QdrantClient
from qdrant_client import models

import os
from dotenv import load_dotenv

load_dotenv()

class HybridSearcher:
    DENSE_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    SPARSE_MODEL = "prithivida/Splade_PP_en_v1"
    def __init__(self, collection_name):
        self.collection_name = collection_name
        
        self.qdrant_client = QdrantClient(
            url="https://73b06d75-0bac-4fa7-9114-9245441a4d2c.us-east4-0.gcp.cloud.qdrant.io:6333", 
            api_key=os.getenv("QDRANT_KEY")
        )
        self.qdrant_client.set_model(self.DENSE_MODEL)

    def search(self, text: str, city=None):
        if city:
            city_filter = models.Filter(
                must=[
                    models.FieldCondition(
                        key="city", 
                        match=models.MatchValue(value=city)
                    )
                ]
            )
        search_result = self.qdrant_client.query(
            collection_name=self.collection_name,
            query_text=text,
            query_filter=city_filter if city else None,
            limit=5,
        )
        metadata = [hit.metadata for hit in search_result]
        return metadata
