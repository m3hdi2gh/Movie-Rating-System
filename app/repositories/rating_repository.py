"""Rating repository for database operations."""

from sqlalchemy.orm import Session

from app.models import MovieRating


class RatingRepository:
    """Repository for rating-related database operations."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, movie_id: int, score: int) -> MovieRating:
        """Create a new rating for a movie."""
        rating = MovieRating(movie_id=movie_id, score=score)
        self.db.add(rating)
        self.db.commit()
        self.db.refresh(rating)
        return rating