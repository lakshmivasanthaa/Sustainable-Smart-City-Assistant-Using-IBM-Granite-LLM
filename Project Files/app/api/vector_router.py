from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from app.services.pinecone_client import get_pinecone_index

router = APIRouter()
model = SentenceTransformer("all-MiniLM-L6-v2")
index = get_pinecone_index()

# Upload Policy
@router.post("/vector/upload", tags=["Vector Search"])
async def upload_policy(file: UploadFile = File(...)):
    try:
        content = await file.read()
        text = content.decode("utf-8")
        embedding = model.encode(text).tolist()
        index.upsert([(file.filename, embedding, {"text": text})])
        return {"message": "Uploaded successfully", "doc_id": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Search Policy (MUST be here)
class SearchRequest(BaseModel):
    query: str
    top_k: int = 3

@router.post("/vector/search-policy", tags=["Vector Search"])
async def search_policy(data: SearchRequest):
    try:
        embedding = model.encode(data.query).tolist()
        results = index.query(vector=embedding, top_k=data.top_k, include_metadata=True)
        return [
            {"score": match["score"], "text": match["metadata"]["text"]}
            for match in results["matches"]
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
