from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# PUBLIC_INTERFACE
class Recommendation(BaseModel):
    video_id: int
    title: str
    thumbnail_url: str

# PUBLIC_INTERFACE
class RecommendationsResponse(BaseModel):
    items: List[Recommendation]

@router.get("/", response_model=RecommendationsResponse, summary="Get recommended videos")
def recommended():
    """
    Returns current user's video recommendations (personalized and/or trending).
    """
    # (Stub)
    return RecommendationsResponse(items=[])
