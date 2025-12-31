"""Rating service for business logic."""

from sqlalchemy.orm import Session

from app.repositories import MovieRepository, RatingRepository
from app.exceptions import NotFoundException, ValidationException
from app.logging_config import logger


class RatingService:
    """Service for rating-related business logic."""

    def __init__(self, db: Session):
        self.db = db
        self.movie_repo = MovieRepository(db)
        self.rating_repo = RatingRepository(db)

    def create_rating(self, movie_id: int, score: int) -> dict:
        """
        Create a rating for a movie.
        Raises NotFoundException if movie not found.
        Raises ValidationException if score is invalid.
        """
        # Log start of operation
        logger.info(f"Rating movie (movie_id={movie_id}, score={score})")

        # Validate score
        if not 1 <= score <= 10:
            logger.warning(
                f"Invalid rating value (movie_id={movie_id}, score={score})"
            )
            raise ValidationException(message="Score must be an integer between 1 and 10")

        # Check if movie exists
        if not self.movie_repo.exists(movie_id):
            logger.warning(f"Movie not found for rating (movie_id={movie_id})")
            raise NotFoundException(message="Movie not found")

        try:
            # Create rating
            rating = self.rating_repo.create(movie_id=movie_id, score=score)

            # Log success
            logger.info(
                f"Rating saved successfully (movie_id={movie_id}, "
                f"score={score}, rating_id={rating.id})"
            )

            return {
                "rating_id": rating.id,
                "movie_id": rating.movie_id,
                "score": rating.score,
                "created_at": rating.rated_at,
            }

        except Exception as e:
            logger.error(
                f"Failed to save rating (movie_id={movie_id}, score={score}): {str(e)}",
                exc_info=True
            )
            raise