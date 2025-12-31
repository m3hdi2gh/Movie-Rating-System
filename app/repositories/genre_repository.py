"""Genre repository for database operations."""

from typing import List, Optional
from sqlalchemy.orm import Session

from app.models import Genre


class GenreRepository:
    """Repository for genre-related database operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, genre_id: int) -> Optional[Genre]:
        """Get a genre by ID."""
        return self.db.query(Genre).filter(Genre.id == genre_id).first()

    def get_by_ids(self, genre_ids: List[int]) -> List[Genre]:
        """Get multiple genres by their IDs."""
        return self.db.query(Genre).filter(Genre.id.in_(genre_ids)).all()

    def exists(self, genre_id: int) -> bool:
        """Check if a genre exists by ID."""
        result = self.db.query(Genre.id).filter(Genre.id == genre_id).first()
        return result is not None

    def all_exist(self, genre_ids: List[int]) -> bool:
        """Check if all given genre IDs exist."""
        if not genre_ids:
            return True
        count = self.db.query(Genre).filter(Genre.id.in_(genre_ids)).count()
        return count == len(genre_ids)