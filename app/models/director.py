from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Director(BaseModel):
    __tablename__ = "directors"

    name = Column(String(255), nullable=False)
    birth_year = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)

    # Relationship: one director -> many movies
    movies = relationship("Movie", back_populates="director")