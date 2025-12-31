"""Rating schemas."""

from datetime import datetime
from pydantic import BaseModel, Field


class RatingCreate(BaseModel):
    """Schema for creating a rating."""

    score: int = Field(..., ge=1, le=10)


class RatingResponse(BaseModel):
    """Schema for rating response."""

    rating_id: int
    movie_id: int
    score: int
    created_at: datetime

    model_config = {"from_attributes": True}