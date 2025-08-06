from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter()

# PUBLIC_INTERFACE
class HistoryItem(BaseModel):
    video_id: int
    title: str
    watched_at: datetime

# PUBLIC_INTERFACE
class WatchHistoryResponse(BaseModel):
    items: List[HistoryItem]

@router.get("/", response_model=WatchHistoryResponse, summary="Get viewing history")
def get_history():
    """
    Returns user's watch/viewing history.
    """
    # (Stub)
    return WatchHistoryResponse(items=[])

@router.post("/add", summary="Add watch event to history")
def add_history(video_id: int):
    """
    Register a new 'watched' event for the current user.
    """
    return {"ok": True}
