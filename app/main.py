from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions import AppException
from app.controllers import movie_router

app = FastAPI(
    title="Movie Rating System",
    description="Backend API for managing movies and ratings",
    version="1.0.0"
)


# =============================================================================
# Exception Handlers
# =============================================================================

@app.exception_handler(AppException)
async def app_exception_handler(_request: Request, exc: AppException):
    """Handle all application exceptions."""
    return JSONResponse(
        status_code=exc.code,
        content={
            "status": "failure",
            "error": {
                "code": exc.code,
                "message": exc.message
            }
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(_request: Request, _exc: Exception):
    """Handle unexpected exceptions."""
    return JSONResponse(
        status_code=500,
        content={
            "status": "failure",
            "error": {
                "code": 500,
                "message": "Internal server error"
            }
        }
    )


# =============================================================================
# Routers
# =============================================================================

app.include_router(movie_router, prefix="/api/v1", tags=["Movies"])


# =============================================================================
# Root Endpoints
# =============================================================================

@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "Welcome to Movie Rating System API"}


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}