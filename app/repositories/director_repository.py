"""Director repository for database operations."""

from typing import Optional
from sqlalchemy.orm import Session

from app.models import Director


class DirectorRepository:
    """Repository for director-related database operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, director_id: int) -> Optional[Director]:
        """Get a director by ID."""
        return self.db.query(Director).filter(Director.id == director_id).first()

    def exists(self, director_id: int) -> bool:
        """Check if a director exists by ID."""
        result = self.db.query(Director.id).filter(Director.id == director_id).first()
        return result is not None