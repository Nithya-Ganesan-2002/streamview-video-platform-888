from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, Field

router = APIRouter()

# PUBLIC_INTERFACE
class RegisterRequest(BaseModel):
    email: EmailStr = Field(..., description="User email address")
    username: str = Field(..., min_length=3, max_length=30)
    password: str = Field(..., min_length=6)

# PUBLIC_INTERFACE
class AuthResponse(BaseModel):
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer", description="JWT token type (bearer)")

# PUBLIC_INTERFACE
class PasswordResetRequest(BaseModel):
    email: EmailStr = Field(..., description="Registered user email")

# PUBLIC_INTERFACE
class PasswordResetSubmit(BaseModel):
    token: str = Field(..., description="Reset token")
    new_password: str = Field(..., min_length=6)

# Registration endpoint
@router.post("/register", response_model=AuthResponse, summary="User Registration")
def register_user(data: RegisterRequest):
    """
    Register new user and return JWT on success.
    """
    # (Stub logic: Add DB insert and validation)
    return AuthResponse(access_token="stub.jwt.token", token_type="bearer")

# Login endpoint
@router.post("/login", response_model=AuthResponse, summary="User Login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate user using username/email and password (password flow). Returns JWT.
    """
    # (Stub logic)
    if form_data.username == "demo" and form_data.password == "demo":
        return AuthResponse(access_token="stub.jwt.token", token_type="bearer")
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

# Logout is frontend-side (stateless JWT); optionally add token blocklist.

# Password reset (start)
@router.post("/forgot-password", status_code=200, summary="Request Password Reset")
def forgot_password(data: PasswordResetRequest):
    """
    Send password reset link to user's email.
    """
    # (Stub logic: Send email link)
    return {"detail": "Password reset email sent."}

# Password reset (submit)
@router.post("/reset-password", status_code=200, summary="Complete Password Reset")
def reset_password(data: PasswordResetSubmit):
    """
    Set new password given valid reset token.
    """
    # (Stub logic)
    return {"detail": "Password successfully updated."}
