from fastapi import APIRouter, UploadFile, File, Query, Depends
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

router = APIRouter()

# PUBLIC_INTERFACE
class Video(BaseModel):
    id: int
    title: str
    description: str
    upload_time: datetime
    channel_id: int
    channel_name: str
    thumbnail_url: str
    video_url: str
    views: int
    duration_seconds: int
    is_live: bool = False

# PUBLIC_INTERFACE
class VideoUploadRequest(BaseModel):
    title: str = Field(..., max_length=255)
    description: str = Field("", description="Video description")

# PUBLIC_INTERFACE
class VideoListResponse(BaseModel):
    count: int
    videos: List[Video]

@router.get("/", response_model=VideoListResponse, summary="Browse videos")
def list_videos(
    q: Optional[str] = Query(None, description="Search term"),
    limit: int = 20,
    offset: int = 0,
):
    """
    List all videos, searchable by title/description.
    """
    return VideoListResponse(
        count=1,
        videos=[Video(
            id=1,
            title="First Video",
            description="Example description",
            upload_time=datetime.now(),
            channel_id=1,
            channel_name="Demo Channel",
            thumbnail_url="https://cdn.example.com/thumb1.png",
            video_url="https://cdn.example.com/video1.mp4",
            views=100,
            duration_seconds=195,
            is_live=False,
        )]
    )

@router.get("/my", response_model=VideoListResponse, summary="My uploaded videos")
def my_videos():
    """
    List videos uploaded by the requesting user.
    """
    return VideoListResponse(count=0, videos=[])

@router.post("/upload", response_model=Video, summary="Upload new video")
def upload_video(
    meta: VideoUploadRequest = Depends(),
    file: UploadFile = File(...),
):
    """
    Upload a new video file. Returns metadata for new video.
    """
    # (Stub: Save file to storage/CDN, extract metadata, store in DB, etc)
    return Video(
            id=2, title=meta.title, description=meta.description,
            upload_time=datetime.now(), channel_id=1,
            channel_name="Demo Channel", thumbnail_url="https://cdn.example.com/thumb2.png",
            video_url="https://cdn.example.com/video2.mp4", views=0, duration_seconds=300, is_live=False
    )

@router.get("/{video_id}", response_model=Video, summary="Get video details")
def video_info(video_id: int):
    """
    Fetch metadata about a video.
    """
    return Video(
        id=video_id, title="Sample", description="Sample Video",
        upload_time=datetime.now(), channel_id=1, channel_name="Demo",
        thumbnail_url="https://cdn.example.com/thumb1.png", video_url="https://cdn.example.com/video1.mp4",
        views=250, duration_seconds=305, is_live=False
    )

@router.put("/{video_id}", response_model=Video, summary="Update video details")
def update_video(video_id: int, changes: VideoUploadRequest):
    """
    Update metadata for a given video.
    """
    return Video(
        id=video_id, title=changes.title, description=changes.description or "",
        upload_time=datetime.now(), channel_id=1, channel_name="Demo",
        thumbnail_url="https://cdn.example.com/thumb1.png", video_url="https://cdn.example.com/video1.mp4",
        views=250, duration_seconds=305, is_live=False
    )

@router.delete("/{video_id}", status_code=204, summary="Delete video")
def delete_video(video_id: int):
    """
    Delete a video the user owns.
    """
    return

@router.get("/by-channel/{channel_id}", response_model=VideoListResponse, summary="List videos by channel/user")
def videos_by_channel(channel_id: int):
    """
    List all videos from a specific channel or user.
    """
    return VideoListResponse(count=0, videos=[])
