import uvicorn

# Import the FastAPI app instance from the actual API package
from src.api.main import app

if __name__ == "__main__":
    # PUBLIC_INTERFACE
    # Entrypoint to launch the FastAPI backend for local dev or container preview.
    # - Binds to 0.0.0.0 for Docker/cloud compatibility (external visibility)
    # - Uses port 3001 as required by project spec
    # - Reload=True is safe for development; set to False in production
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=3001,
        reload=True,
    )
