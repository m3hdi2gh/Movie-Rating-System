from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Genre(BaseModel):
    __tablename__ = "genres"

    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)

    # Relationship: Many-to-Many with Movie via association table
    movies = relationship(
        "Movie",
        secondary="movie_genres",
        back_populates="genres"
    )