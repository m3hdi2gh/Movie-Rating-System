"""Director schemas."""

from typing import Optional
from pydantic import BaseModel


class DirectorBrief(BaseModel):
    """Brief director info for movie list responses."""

    id: int
    name: str

    model_config = {"from_attributes": True}


class DirectorResponse(BaseModel):
    """Full director info for movie detail responses."""

    id: int
    name: str
    birth_year: Optional[int] = None
    description: Optional[str] = None

    model_config = {"from_attributes": True}