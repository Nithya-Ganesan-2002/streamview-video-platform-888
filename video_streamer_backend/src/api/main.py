from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import endpoints from feature modules
from .routers import (
    auth,
    users,
    videos,
    streaming,
    payments,
    history,
    recommendations
)

# Meta for OpenAPI
app = FastAPI(
    title="StreamView Video Platform API",
    description="Backend API for video streaming platform: manages authentication, user profiles, video management, uploads, streaming, payments, watch history and recommendations.",
    version="1.0.0",
    openapi_tags=[
        {"name": "auth", "description": "User authentication, registration, login/logout."},
        {"name": "users", "description": "User profile operations."},
        {"name": "videos", "description": "View, search, upload, manage videos."},
        {"name": "streaming", "description": "Live and on-demand video streaming."},
        {"name": "payments", "description": "Payments, billing, premium features."},
        {"name": "history", "description": "Watch and search history."},
        {"name": "recommendations", "description": "Video recommendations for users."},
    ]
)

# CORS (allow localhost, frontend dev hosts)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/", tags=["health"])
def health_check():
    """API health check endpoint."""
    return {"message": "Healthy"}

# Routers for each feature domain
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(videos.router, prefix="/videos", tags=["videos"])
app.include_router(streaming.router, prefix="/stream", tags=["streaming"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(history.router, prefix="/history", tags=["history"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
