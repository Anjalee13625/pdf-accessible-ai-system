from fastapi import APIRouter
from firebase import db

router = APIRouter()

@router.post("/login")
def login(user: dict):
    return {"message": "Login handled by Firebase frontend"}
