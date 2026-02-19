from fastapi import APIRouter, UploadFile, File
from firebase import db
from backend.core_pipeline.ai_pipeline import process_pdf
from datetime import datetime
import uuid
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{file_id}.pdf"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    process_pdf(file_path)

    db.collection("uploads").add({
        "file_id": file_id,
        "filename": file.filename,
        "timestamp": datetime.utcnow()
    })

    return {"message": "PDF processed", "file_id": file_id}
