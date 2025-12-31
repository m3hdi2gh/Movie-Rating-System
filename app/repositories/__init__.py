"""Repository layer for data access."""

from app.repositories.base import BaseRepository
from app.repositories.movie_repository import MovieRepository
from app.repositories.rating_repository import RatingRepository
from app.repositories.director_repository import DirectorRepository
from app.repositories.genre_repository import GenreRepository

__all__ = [
    "BaseRepository",
    "MovieRepository",
    "RatingRepository",
    "DirectorRepository",
    "GenreRepository",
]