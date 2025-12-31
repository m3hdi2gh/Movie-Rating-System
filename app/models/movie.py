from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Movie(BaseModel):
    __tablename__ = "movies"

    title = Column(String(255), nullable=False)
    release_year = Column(Integer, nullable=True)
    cast = Column(Text, nullable=True)
    description = Column(Text, nullable=True)

    # Foreign Key to Director
    director_id = Column(Integer, ForeignKey("directors.id"), nullable=True)

    # Relationships
    director = relationship("Director", back_populates="movies")

    genres = relationship(
        "Genre",
        secondary="movie_genres",
        back_populates="movies"
    )

    ratings = relationship(
        "MovieRating",
        back_populates="movie",
        cascade="all, delete-orphan"
    )