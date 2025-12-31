"""Movie schemas."""

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field

from app.schemas.director import DirectorBrief, DirectorResponse


class MovieCreate(BaseModel):
    """Schema for creating a movie."""

    title: str = Field(..., min_length=1, max_length=255)
    director_id: int
    release_year: Optional[int] = Field(None, ge=1800, le=2100)
    cast: Optional[str] = None
    genres: List[int] = Field(default_factory=list)


class MovieUpdate(BaseModel):
    """Schema for updating a movie."""

    title: Optional[str] = Field(None, min_length=1, max_length=255)
    director_id: Optional[int] = None
    release_year: Optional[int] = Field(None, ge=1800, le=2100)
    cast: Optional[str] = None
    genres: Optional[List[int]] = None


class MovieListItem(BaseModel):
    """Schema for movie in list responses."""

    id: int
    title: str
    release_year: Optional[int] = None
    director: Optional[DirectorBrief] = None
    genres: List[str] = Field(default_factory=list)
    average_rating: Optional[float] = None
    ratings_count: int = 0

    model_config = {"from_attributes": True}


class MovieDetail(BaseModel):
    """Schema for movie detail response."""

    id: int
    title: str
    release_year: Optional[int] = None
    director: Optional[DirectorResponse] = None
    genres: List[str] = Field(default_factory=list)
    cast: Optional[str] = None
    average_rating: Optional[float] = None
    ratings_count: int = 0

    model_config = {"from_attributes": True}


class MovieCreateResponse(BaseModel):
    """Schema for movie creation response."""

    id: int
    title: str
    release_year: Optional[int] = None
    director: Optional[DirectorBrief] = None
    genres: List[str] = Field(default_factory=list)
    cast: Optional[str] = None
    average_rating: Optional[float] = None
    ratings_count: int = 0

    model_config = {"from_attributes": True}


class MovieUpdateResponse(BaseModel):
    """Schema for movie update response."""

    id: int
    title: str
    release_year: Optional[int] = None
    director: Optional[DirectorBrief] = None
    genres: List[str] = Field(default_factory=list)
    cast: Optional[str] = None
    average_rating: Optional[float] = None
    ratings_count: int = 0
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}