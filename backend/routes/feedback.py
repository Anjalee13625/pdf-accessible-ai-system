from fastapi import APIRouter
from firebase import db
from datetime import datetime

router = APIRouter()

@router.post("/")
def submit_feedback(data: dict):
    db.collection("feedback").add({
        "rating": data.get("rating"),
        "comment": data.get("comment"),
        "timestamp": datetime.utcnow()
    })
    return {"message": "Feedback saved"}
