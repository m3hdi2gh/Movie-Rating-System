"""Controller layer - API endpoints."""

from app.controllers.movie_controller import router as movie_router

__all__ = [
    "movie_router",
]