# Project Repository

This is the initial README file for the project.

---

## FastAPI Backend (`video_streamer_backend`) Startup/Preview Instructions

**Run the FastAPI backend (local or in preview):**

```bash
cd video_streamer_backend
# Ensure all deps are installed:
pip install -r requirements.txt
# Start on port 3001:
python main.py
```

**Expected behavior:**
- The API server will bind to `0.0.0.0:3001` (default as per `main.py`).
- Health check endpoint: [http://localhost:3001/](http://localhost:3001/) — returns `{"message": "Healthy"}` on success.
- The server uses `reload=True` in development (auto-reloads on code change).
- If you see errors about imports/modules or dependencies, check that you are running from the `video_streamer_backend` directory, and that all dependencies are installed.

**Troubleshooting:**
- All Python packages required are in `requirements.txt`.
- If you get `ModuleNotFoundError` for `fastapi` or `uvicorn`, ensure you installed the dependencies in your virtual environment.
- The main FastAPI `app` instance is defined in `src/api/main.py` and imported in the top-level `main.py`.
- If running in Docker, ensure port 3001 is exposed.

**Project Structure Expectation:**
- All routers are in `src/api/routers/`
- Main app wiring is in `src/api/main.py`
- Entrypoint for Uvicorn/dev server is `main.py` (top-level).

**OpenAPI Docs**
- [http://localhost:3001/docs](http://localhost:3001/docs) — Swagger UI
- [http://localhost:3001/redoc](http://localhost:3001/redoc) — ReDoc
