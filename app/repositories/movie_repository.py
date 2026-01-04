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

    def create(self, data: dict) -> Movie:
        """Create a new movie."""
        movie = Movie(
            title=data["title"],
            director_id=data["director_id"],
            release_year=data.get("release_year"),
            cast=data.get("cast"),
        )
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie

    def update(self, movie: Movie, data: dict) -> Movie:
        """Update an existing movie."""
        if "title" in data and data["title"] is not None:
            movie.title = data["title"]
        if "director_id" in data and data["director_id"] is not None:
            movie.director_id = data["director_id"]
        if "release_year" in data:
            movie.release_year = data["release_year"]
        if "cast" in data:
            movie.cast = data["cast"]

        self.db.commit()
        self.db.refresh(movie)
        return movie

    def delete(self, movie: Movie) -> None:
        """Delete a movie."""
        self.db.delete(movie)
        self.db.commit()

    def sync_genres(self, movie: Movie, genres: List[Genre]) -> None:
        """Sync movie genres (replace existing with new ones)."""
        movie.genres = genres
        self.db.commit()
        self.db.refresh(movie)