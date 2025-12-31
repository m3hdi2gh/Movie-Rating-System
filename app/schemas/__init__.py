"""Pydantic schemas for request/response validation."""

from app.schemas.base import (
    ErrorDetail,
    ErrorResponse,
    SuccessResponse,
    PaginatedData,
    PaginatedResponse,
)
from app.schemas.director import DirectorBrief, DirectorResponse
from app.schemas.genre import GenreResponse
from app.schemas.movie import (
    MovieCreate,
    MovieUpdate,
    MovieListItem,
    MovieDetail,
    MovieCreateResponse,
    MovieUpdateResponse,
)
from app.schemas.rating import RatingCreate, RatingResponse

__all__ = [
    # Base
    "ErrorDetail",
    "ErrorResponse",
    "SuccessResponse",
    "PaginatedData",
    "PaginatedResponse",
    # Director
    "DirectorBrief",
    "DirectorResponse",
    # Genre
    "GenreResponse",
    # Movie
    "MovieCreate",
    "MovieUpdate",
    "MovieListItem",
    "MovieDetail",
    "MovieCreateResponse",
    "MovieUpdateResponse",
    # Rating
    "RatingCreate",
    "RatingResponse",
]