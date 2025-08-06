from fastapi import APIRouter, HTTPException

router = APIRouter()

# PUBLIC_INTERFACE
@router.get("/video/{video_id}", summary="Stream a video file")
def stream_video_file(video_id: int):
    """
    Streams the video file content to the client (supports adaptive/HLS if available).
    Returns raw video content with appropriate headers for player.
    """
    # (Stub: File I/O and range requests not implemented, so just return 404)
    raise HTTPException(status_code=404, detail="Video streaming not implemented in stub.")

# PUBLIC_INTERFACE
@router.get("/live/{channel_id}", summary="Live stream for current channel/user")
def stream_live(channel_id: int):
    """
    Stream live broadcast for a given channel (RTMP/HLS/etc). Stub only.
    """
    raise HTTPException(status_code=501, detail="Live streaming not implemented yet.")
