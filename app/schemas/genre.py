"""Genre schemas."""

from typing import Optional
from pydantic import BaseModel


class GenreResponse(BaseModel):
    """Genre response schema."""

    id: int
    name: str
    description: Optional[str] = None

    model_config = {"from_attributes": True}