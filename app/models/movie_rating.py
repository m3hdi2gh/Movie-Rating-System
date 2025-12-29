from sqlalchemy import Column, Integer, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class MovieRating(Base):
    __tablename__ = "movie_ratings"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, nullable=False)
    rated_at = Column(DateTime(timezone=True), server_default=func.now())

    # Foreign Key to Movie
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"), nullable=False)

    # Relationship
    movie = relationship("Movie", back_populates="ratings")

    # Constraint: score must be between 1 and 10
    __table_args__ = (
        CheckConstraint("score >= 1 AND score <= 10", name="check_score_range"),
    )