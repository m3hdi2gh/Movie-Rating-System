"""Movie service for business logic."""

from typing import Optional, List, Tuple
from sqlalchemy.orm import Session

from app.models import Movie
from app.repositories import MovieRepository
from app.exceptions import NotFoundException
from app.logging_config import logger


class MovieService:
    """Service for movie-related business logic."""

    def __init__(self, db: Session):
        self.db = db
        self.movie_repo = MovieRepository(db)

    def get_movies(
        self,
        page: int = 1,
        page_size: int = 10,
        title: Optional[str] = None,
        release_year: Optional[int] = None,
        genre: Optional[str] = None,
    ) -> Tuple[List[dict], int]:
        """
        Get paginated list of movies with optional filters.
        Returns tuple of (movie_list, total_count).
        """
        # Log start of operation
        logger.info(
            f"Fetching movies list (page={page}, page_size={page_size}, "
            f"title={title}, release_year={release_year}, genre={genre})"
        )

        try:
            movies, total_count = self.movie_repo.get_movies_paginated(
                page=page,
                page_size=page_size,
                title=title,
                release_year=release_year,
                genre=genre,
            )

            # Transform to response format
            movie_list = [self._to_list_item(movie) for movie in movies]

            # Log success
            logger.info(f"Returned {len(movie_list)} movies (total: {total_count})")

            return movie_list, total_count

        except Exception as e:
            logger.error(f"Failed to fetch movies: {str(e)}", exc_info=True)
            raise

    def get_movie_by_id(self, movie_id: int) -> dict:
        """
        Get movie details by ID.
        Raises NotFoundException if not found.
        """
        logger.info(f"Fetching movie details (movie_id={movie_id})")

        try:
            movie = self.movie_repo.get_by_id(movie_id)
            if not movie:
                logger.warning(f"Movie not found (movie_id={movie_id})")
                raise NotFoundException(message="Movie not found")

            logger.info(f"Movie found: {movie.title} (movie_id={movie_id})")
            return self._to_detail(movie)

        except NotFoundException:
            raise
        except Exception as e:
            logger.error(f"Failed to fetch movie (movie_id={movie_id}): {str(e)}", exc_info=True)
            raise

    @staticmethod
    def _calculate_average_rating(movie: Movie) -> Optional[float]:
        """Calculate average rating for a movie."""
        if not movie.ratings:
            return None
        total = sum(r.score for r in movie.ratings)
        return round(total / len(movie.ratings), 1)

    def _to_list_item(self, movie: Movie) -> dict:
        """Transform movie to list item format."""
        return {
            "id": movie.id,
            "title": movie.title,
            "release_year": movie.release_year,
            "director": {
                "id": movie.director.id,
                "name": movie.director.name,
            } if movie.director else None,
            "genres": [g.name for g in movie.genres],
            "average_rating": self._calculate_average_rating(movie),
            "ratings_count": len(movie.ratings) if movie.ratings else 0,
        }

    def _to_detail(self, movie: Movie) -> dict:
        """Transform movie to detail format."""
        return {
            "id": movie.id,
            "title": movie.title,
            "release_year": movie.release_year,
            "director": {
                "id": movie.director.id,
                "name": movie.director.name,
                "birth_year": movie.director.birth_year,
                "description": movie.director.description,
            } if movie.director else None,
            "genres": [g.name for g in movie.genres],
            "cast": movie.cast,
            "average_rating": self._calculate_average_rating(movie),
            "ratings_count": len(movie.ratings) if movie.ratings else 0,
        }

    # =========================================================================
    # APIs 5-7: Create, Update, Delete (To be implement by parsa)
    # =========================================================================
    # def create_movie(self, data: MovieCreate) -> dict:
    #     pass
    #
    # def update_movie(self, movie_id: int, data: MovieUpdate) -> dict:
    #     pass
    #
    # def delete_movie(self, movie_id: int) -> None:
    #     pass