"""Movie repository for database operations."""

from typing import Optional, List, Tuple
from sqlalchemy.orm import Session, joinedload

from app.models import Movie, Genre


class MovieRepository:
    """Repository for movie-related database operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_movies_paginated(
        self,
        page: int = 1,
        page_size: int = 10,
        title: Optional[str] = None,
        release_year: Optional[int] = None,
        genre: Optional[str] = None,
    ) -> Tuple[List[Movie], int]:
        """
        Get movies with pagination and optional filters.
        Returns tuple of (movies, total_count).
        """
        query = self.db.query(Movie).options(
            joinedload(Movie.director),
            joinedload(Movie.genres),
            joinedload(Movie.ratings)
        )

        # Apply filters
        if title:
            query = query.filter(Movie.title.ilike(f"%{title}%"))

        if release_year:
            query = query.filter(Movie.release_year == release_year)

        if genre:
            query = query.join(Movie.genres).filter(Genre.name.ilike(f"%{genre}%"))

        # Get total count before pagination
        total_count = query.distinct().count()

        # Apply pagination
        offset = (page - 1) * page_size
        movies = query.distinct().offset(offset).limit(page_size).all()

        return movies, total_count

    def get_by_id(self, movie_id: int) -> Optional[Movie]:
        """Get a movie by ID with all relations loaded."""
        return self.db.query(Movie).options(
            joinedload(Movie.director),
            joinedload(Movie.genres),
            joinedload(Movie.ratings)
        ).filter(Movie.id == movie_id).first()

    def exists(self, movie_id: int) -> bool:
        """Check if a movie exists by ID."""
        result = self.db.query(Movie.id).filter(Movie.id == movie_id).first()
        return result is not None