from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel, EmailStr
from typing import Optional

router = APIRouter()

# PUBLIC_INTERFACE
class UserProfile(BaseModel):
    id: int
    username: str
    email: EmailStr
    display_name: Optional[str]
    avatar_url: Optional[str] = None
    bio: Optional[str] = ""

# PUBLIC_INTERFACE
class UpdateProfileRequest(BaseModel):
    display_name: Optional[str] = ""
    bio: Optional[str] = ""

# PUBLIC_INTERFACE
class UpdateAvatarResponse(BaseModel):
    avatar_url: str

@router.get("/me", response_model=UserProfile, summary="Get current user profile")
def get_my_profile():
    """
    Get current logged-in user's profile info.
    """
    # (Stub - replace with user lookup)
    return UserProfile(id=1, username="demo", email="demo@example.com", display_name="Demo User")

@router.put("/me", response_model=UserProfile, summary="Update current user profile")
def update_my_profile(changes: UpdateProfileRequest):
    """
    Update profile fields (display name, bio).
    """
    # (Stub)
    return UserProfile(id=1, username="demo", email="demo@example.com", display_name=changes.display_name or "Demo User")

@router.post("/me/avatar", response_model=UpdateAvatarResponse, summary="Upload user avatar")
def upload_avatar(file: UploadFile = File(...)):
    """
    Upload user's avatar image. Returns URL after upload (to CDN/storage).
    """
    # (Stub: Save to object storage, generate URL)
    return UpdateAvatarResponse(avatar_url="https://cdn.example.com/avatars/fake-avatar.png")
