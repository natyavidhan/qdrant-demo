from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv
import json
from qdrant_client.models import Distance, VectorParams, PointStruct

load_dotenv()
def main():
    qdrant_client = QdrantClient(
        url="https://73b06d75-0bac-4fa7-9114-9245441a4d2c.us-east4-0.gcp.cloud.qdrant.io:6333", 
        api_key=os.getenv("QDRANT_KEY"),
    )

    qdrant_client.set_model("sentence-transformers/all-MiniLM-L6-v2")

    if not qdrant_client.collection_exists("startups"):
        qdrant_client.create_collection(
            collection_name="startups",
            vectors_config=qdrant_client.get_fastembed_vector_params()
        )

    payload_path = "data/startups_demo.json"
    metadata = []
    documents = []

    with open(payload_path) as fd:
        for line in fd:
            obj = json.loads(line)
            documents.append(obj.pop("description"))
            metadata.append(obj)
            

    qdrant_client.add(
        collection_name="startups",
        documents=documents,
        metadata=metadata,
        parallel=0
    )
    
if __name__ == "__main__":
    main()