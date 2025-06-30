from pinecone import Pinecone, ServerlessSpec
from app.core.config import settings

pc = Pinecone(api_key=settings.PINECONE_API_KEY)

if settings.INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=settings.INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",                      # ✅ Use aws (not gcp)
            region=settings.PINECONE_ENV      # ✅ Your .env says us-east-1
        )
    )

index = pc.Index(settings.INDEX_NAME)

def get_pinecone_index():
    return index
