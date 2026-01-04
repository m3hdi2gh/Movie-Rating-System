"""Movie service for business logic."""

from typing import Optional, List, Tuple
from sqlalchemy.orm import Session

from app.models import Movie
from app.repositories import MovieRepository, DirectorRepository, GenreRepository
from app.exceptions import NotFoundException, ValidationException
from app.logging_config import logger


class MovieService:
    """Service for movie-related business logic."""

    def __init__(self, db: Session):
        self.db = db
        self.movie_repo = MovieRepository(db)
        self.director_repo = DirectorRepository(db)
        self.genre_repo = GenreRepository(db)

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

    def create_movie(self, data: dict) -> dict:
        """
        Create a new movie.
        Raises ValidationException if director_id or genres are invalid.
        """
        logger.info(f"Creating movie: {data.get('title')}")

        # Validate director exists
        director_id = data.get("director_id")
        if not self.director_repo.exists(director_id):
            logger.warning(f"Invalid director_id: {director_id}")
            raise ValidationException(message="Invalid director_id or genres")

        # Validate genres exist
        genre_ids = data.get("genres", [])
        if genre_ids and not self.genre_repo.all_exist(genre_ids):
            logger.warning(f"Invalid genre_ids: {genre_ids}")
            raise ValidationException(message="Invalid director_id or genres")

        try:
            # Create movie
            movie = self.movie_repo.create({
                "title": data["title"],
                "director_id": director_id,
                "release_year": data.get("release_year"),
                "cast": data.get("cast"),
            })

            # Sync genres
            if genre_ids:
                genres = self.genre_repo.get_by_ids(genre_ids)
                self.movie_repo.sync_genres(movie, genres)

            # Reload movie with relations
            movie = self.movie_repo.get_by_id(movie.id)

            logger.info(f"Movie created successfully (movie_id={movie.id})")
            return self._to_create_response(movie)

        except Exception as e:
            logger.error(f"Failed to create movie: {str(e)}", exc_info=True)
            raise

    def update_movie(self, movie_id: int, data: dict) -> dict:
        """
        Update an existing movie.
        Raises NotFoundException if movie not found.
        Raises ValidationException if director_id or genres are invalid.
        """
        logger.info(f"Updating movie (movie_id={movie_id})")

        # Check movie exists
        movie = self.movie_repo.get_by_id(movie_id)
        if not movie:
            logger.warning(f"Movie not found (movie_id={movie_id})")
            raise NotFoundException(message="Movie not found")

        # Validate director if provided
        director_id = data.get("director_id")
        if director_id is not None and not self.director_repo.exists(director_id):
            logger.warning(f"Invalid director_id: {director_id}")
            raise ValidationException(message="Invalid director_id or genres")

        # Validate genres if provided
        genre_ids = data.get("genres")
        if genre_ids is not None and genre_ids and not self.genre_repo.all_exist(genre_ids):
            logger.warning(f"Invalid genre_ids: {genre_ids}")
            raise ValidationException(message="Invalid director_id or genres")

        try:
            # Update movie fields
            update_data = {}
            if "title" in data:
                update_data["title"] = data["title"]
            if "director_id" in data:
                update_data["director_id"] = data["director_id"]
            if "release_year" in data:
                update_data["release_year"] = data["release_year"]
            if "cast" in data:
                update_data["cast"] = data["cast"]

            if update_data:
                movie = self.movie_repo.update(movie, update_data)

            # Sync genres if provided
            if genre_ids is not None:
                genres = self.genre_repo.get_by_ids(genre_ids) if genre_ids else []
                self.movie_repo.sync_genres(movie, genres)

            # Reload movie with relations
            movie = self.movie_repo.get_by_id(movie.id)

            logger.info(f"Movie updated successfully (movie_id={movie_id})")
            return self._to_update_response(movie)

        except Exception as e:
            logger.error(f"Failed to update movie (movie_id={movie_id}): {str(e)}", exc_info=True)
            raise

    def delete_movie(self, movie_id: int) -> None:
        """
        Delete a movie.
        Raises NotFoundException if movie not found.
        """
        logger.info(f"Deleting movie (movie_id={movie_id})")

        # Check movie exists
        movie = self.movie_repo.get_by_id(movie_id)
        if not movie:
            logger.warning(f"Movie not found (movie_id={movie_id})")
            raise NotFoundException(message="Movie not found")

        try:
            self.movie_repo.delete(movie)
            logger.info(f"Movie deleted successfully (movie_id={movie_id})")

        except Exception as e:
            logger.error(f"Failed to delete movie (movie_id={movie_id}): {str(e)}", exc_info=True)
            raise

    # =========================================================================
    # Helper methods
    # =========================================================================

    def _calculate_average_rating(self, movie: Movie) -> Optional[float]:
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

    def _to_create_response(self, movie: Movie) -> dict:
        """Transform movie to create response format."""
        return {
            "id": movie.id,
            "title": movie.title,
            "release_year": movie.release_year,
            "director": {
                "id": movie.director.id,
                "name": movie.director.name,
            } if movie.director else None,
            "genres": [g.name for g in movie.genres],
            "cast": movie.cast,
            "average_rating": None,
            "ratings_count": 0,
        }

    def _to_update_response(self, movie: Movie) -> dict:
        """Transform movie to update response format."""
        return {
            "id": movie.id,
            "title": movie.title,
            "release_year": movie.release_year,
            "director": {
                "id": movie.director.id,
                "name": movie.director.name,
            } if movie.director else None,
            "genres": [g.name for g in movie.genres],
            "cast": movie.cast,
            "average_rating": self._calculate_average_rating(movie),
            "ratings_count": len(movie.ratings) if movie.ratings else 0,
            "updated_at": movie.updated_at,
        }