from sqlalchemy import Column, Integer, ForeignKey, Table
from app.db.database import Base

# Bridge table for Many-to-Many relationship between Movie and Genre
movie_genres = Table(
    "movie_genres",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id", ondelete="CASCADE"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id", ondelete="CASCADE"), primary_key=True)
)